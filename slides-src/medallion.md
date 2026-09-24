---
marp: true
theme: charcoal-lb
paginate: true
---

<!-- _class: lead -->
<!-- _paginate: false -->

# Medallion Architecture
## Bronze, silver, gold — and why your data needs all three

IS 640 — Business Application Programming

<!--
This one is a field trip out of Python and into where the data actually
lives. Nobody hands you a clean dataset in the wild -- they hand you
seven systems that disagree with each other, and medallion architecture
is the pattern the industry settled on for turning that into something
you can query without crying.

Source for everything here is the Databricks blog "What is a Medallion
Architecture?" -- worth reading in full, it is short.
-->

---

## Every system thinks it is the only system

- Sales lives in the CRM
- Inventory lives in the warehouse system
- The factory floor emits sensor data nobody has ever joined to anything
- Finance has a spreadsheet, and it is load-bearing

<!--
This is the data silo problem and every organization has it. None of
these systems were designed to talk to each other; they were each bought
to solve one department's problem, and they each solved it.

Ask the room where they have seen this -- anyone who has worked in a
mid-sized company has a story, and the spreadsheet one is always true.

The valuable questions are the ones that cross these boundaries. The
blog's example is joining manufacturing sensor data to sales returns to
find defects, which no single system above could answer alone. So the
architecture's whole job is making the crossing cheap.
-->

---

## Medallion architecture, in one sentence

**Medallion architecture:** a design pattern that organizes lakehouse data
into layers, each one incrementally improving structure and quality

Also called **multi-hop** — the data hops from layer to layer.

<!--
Read the definition and then translate it: instead of one heroic job
that reads from seven sources and writes one perfect table, you take
small steps, and every step is saved.

The olympic medal naming is doing real work here -- bronze, silver, gold
tells you the direction of travel without anyone having to explain it,
which is most of why this pattern won.
-->

---

## Three layers, one direction

| Layer | Holds | Written for |
|-|-|-|
| **Bronze** | Raw data, exactly as it arrived | Auditors and reprocessing |
| **Silver** | Cleaned, deduplicated, conformed | Analysts and data scientists |
| **Gold** | Business-ready aggregates | Dashboards and executives |

Data only flows down the table, never back up.

<!--
That last line is the rule that keeps the whole thing honest. Gold never
writes back into silver, silver never writes back into bronze. One
direction means you can always replay the pipeline from the top and get
the same answer.
-->

---

## The kitchen version

- **Bronze** — groceries dumped on the counter, bags and all
- **Silver** — washed, peeled, chopped, the bad onion thrown out
- **Gold** — dinner, plated, garnished, photographed for Instagram

<!--
Nobody eats the grocery bag. But you also do not throw the bag away
until dinner is safely on the table, because if you ruin the sauce you
want the receipt and the original ingredients.

This analogy is mine, not the blog's, but it survives contact with every
real pipeline I have seen. Use it when someone asks why they cannot just
clean the data on the way in.
-->

---

<!-- _class: lead -->

# Bronze — land it, don't touch it

---

## Bronze keeps the mess on purpose

- Structure matches the source system, warts included
- No business rules, no renaming, no "quick fixes"
- Append-only — history accumulates rather than overwriting

<!--
The discipline here is the hard part, because the instinct when you see
a badly named column is to fix it immediately. Do not. The moment bronze
diverges from the source, you have lost your ability to prove what the
source actually said.

This is also the layer that pays for itself the day something breaks:
because the raw copy still exists, you can reprocess without going back
to the source system -- which may rate-limit you, charge per extract,
purge after 90 days, or belong to a vendor whose contract has ended. A
bug in your cleaning logic becomes a re-run rather than an incident.
-->

---

## The only thing bronze adds is bookkeeping

```python
# Lets stamp each row with where it came from and when
bronze = (raw
    .withColumn("_ingested_at", current_timestamp())
    .withColumn("_source_file", input_file_name())
    .withColumn("_process_id", lit(run_id)))
```

<!--
Metadata columns capturing load timestamps and process IDs -- that is
the blog's language, and it is the entire permitted edit at this layer.

These columns are what make the layer auditable. Six months from now
when a number looks wrong, these three columns tell you which file and
which pipeline run produced the row. Without them you are guessing.
-->

---

<!-- _class: lead -->

# Silver — just enough cleaning

---

## Silver builds the enterprise view

- One master customer record, not five near-duplicates
- Transactions deduplicated and conformed
- Types fixed, keys joined, obvious garbage filtered

<!--
The blog's phrase is "just-enough" cleaning and merging, and the
emphasis belongs on *just enough*. You are building an enterprise view
of the key business entities -- customers, stores, transactions -- that
the whole organization can agree on.

This is the layer where self-service starts. An analyst who knows SQL
can be turned loose on silver and do real ad-hoc work.
-->

---

## Dedupe is most of the job

```sql
-- Lets keep one row per customer, the most recent one
CREATE TABLE silver.customers AS
SELECT * EXCEPT (rn) FROM (
  SELECT *, ROW_NUMBER() OVER (
    PARTITION BY customer_id ORDER BY _ingested_at DESC) AS rn
  FROM bronze.customers)
WHERE rn = 1;
```

<!--
Walk this one slowly -- window functions are new to most of the room.
PARTITION BY groups the rows per customer, ORDER BY puts the newest
first, ROW_NUMBER labels them, and we keep number one.

This pattern shows up in roughly every silver layer ever built, so it is
worth recognizing on sight.
-->

---

## ELT, not ETL

Load first, transform later — **speed and agility to ingest** beats
getting it perfect on the way in.

<!--
Traditional warehouses transform before loading, so the transformation
has to be right before any data lands anywhere. The lakehouse flips the
last two letters: extract, load, then transform.

Three reasons it won. Storage is cheap now, so keeping the raw copy is
no longer the expensive choice. You can replay, because the untransformed
data still exists. And you do not have to know every question in advance
-- under ETL, a column you discarded at ingestion is gone forever.

Practically, the heavy project-specific business rules are deferred to
the silver-to-gold hop. Silver stays general on purpose, because the
moment you bake one team's rules into it, it stops being an enterprise
view and becomes that team's table.
-->

---

<!-- _class: lead -->

# Gold — answers, not data

---

## Gold is shaped by the question

- Customer segmentation
- Product quality analytics
- Inventory and marketing analytics

De-normalized and read-optimized — fewer joins, faster dashboards.

<!--
Those are the blog's own examples. Notice they are named after business
problems, not after source systems -- that is the tell that you are
looking at a gold table.

If you have taken a database course: Kimball star schemas and Inmon data
marts both live here. Gold is where the classical warehouse modeling you
may already know finally shows up in the lakehouse.
-->

---

## One gold table, one audience

```sql
-- Lets build the table the returns dashboard actually needs
CREATE TABLE gold.returns_by_product AS
SELECT product_line,
       COUNT(*) AS units,
       AVG(returned) AS return_rate
FROM silver.units JOIN silver.returns USING (unit_id)
GROUP BY product_line;
```

<!--
Six lines, and it only reads this cleanly because bronze and silver did
the unglamorous work first. The join works because silver already
conformed the keys.

Point out that this table is a dead end by design. It is project
specific, it is allowed to be redundant with other gold tables, and if
the dashboard changes you rebuild it from silver rather than patching it.
-->

---

## What the pattern buys you

- A model you can explain to a new hire in five minutes
- Incremental processing instead of full reloads
- Any table rebuildable from raw, at any time
- ACID transactions and time travel, via Delta Lake

<!--
That third one deserves saying out loud: every table below bronze is
disposable. Delete gold entirely and you can rebuild it, because the
inputs and the code both still exist.

Time travel means querying the table as of last Tuesday, which turns
"the dashboard changed and nobody knows why" from an investigation into
a query.

One more structural point from the blog: bronze and silver tables fan
out one-to-many into downstream tables, which is what makes this pattern
compatible with a data mesh -- one silver table legitimately feeding
many gold tables owned by different teams.
-->

---

<!-- _class: lead -->

# Recap

- Bronze is fidelity, silver is trust, gold is answers
- Each hop improves structure and quality, one direction only
- Keep raw forever so every mistake is a re-run, not an incident
- Load first and transform later — ELT, not ETL

<!--
If they remember one sentence, make it the first bullet. Bronze is
fidelity, silver is trust, gold is answers -- that framing survives
whatever vendor's tooling they end up using, and the vendors all
implement this same pattern under different product names.
-->

---

<!-- _class: lead -->

# Questions?

<!--
Good closing prompt if the room is quiet: ask which layer the finance
spreadsheet belongs in. The honest answer is that it is a source system,
which usually lands the point better than anything on the slides did.
-->

---
marp: true
theme: charcoal-lb
---

<!--
Reference sheet of slide patterns. This file is NOT built -- build_slides.py
skips anything starting with '_'. Copy a block out of here when writing a deck.
-->

# Title slide

```
---
marp: true
theme: charcoal-lb
paginate: true
---

<!-- _class: lead -->
<!-- _paginate: false -->

# Chapter N
## Subtitle in one line

IS 640 — Business Application Programming
```

`_class: lead` centres the slide and enlarges the H1. `_paginate: false` keeps
the page number off the title slide. The leading underscore means "this slide
only".

---

# Section break

```
---

<!-- _class: lead -->

# 2.4 Numeric Types
```

Use these to signal a new topic. One line, nothing else.

---

# One idea per slide

```
---

## Variables

**Variable:**
Named item, such as x, y, john, lamp.

- Always starts on the left of `=`
- Must start with a letter
```

Keep to a heading plus 3-5 bullets. If it needs more, it is two slides.

---

# Code with narration

```
---

## Assigning a variable

​```
# Lets show the value
x = 13
print(x)
​```

Output: `13`
```

Bare fences, no language tag — matches the house style in the notes. 3-8 lines
of code; anything longer does not read from the back of the room.

---

# Two columns

```
---

<div class="columns">
<div>

## Do this
`x = 13` ✅

</div>
<div>

## Not this
`5 = x` ❌

</div>
</div>
```

Needs the `.columns` rule in `lb-components.css`. Good for right/wrong pairs.

---

# Speaker notes

```
---

## Slide title

Visible bullet

<!--
This text only shows in presenter view (press P).
Put the "say this out loud" version here.
-->
```

---

# Image slide

```
---

## The interpreter

![w:800](assets/PythonInterpreter.png)
```

`![w:800]` sets width in px, `![h:400]` height. Images referenced from a deck
must live in `slides-src/assets/`, which build_slides.py copies next to the
built HTML.

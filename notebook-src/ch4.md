# Chapter 4: Branching

Practice writing if branches, if-else, elif chains, and the operators that drive them.

## 4.1 If-else branches — if branch

An if branch is a block of statements that only runs when its condition is
True. The condition line ends in a colon, and the block underneath it is
indented.

```python
years_active = 8
discount = 0

# TODO: write an if branch that sets discount to 0.10 when years_active is
#       greater than 5, then print discount
```

## 4.1 If-else branches — if-else branch

An if-else branch always runs exactly one of its two blocks — never both,
never neither.

```python
driver_age = 30

# TODO: write an if-else branch that sets insure_price to 4800 if driver_age
#       is less than 25, and 2200 otherwise, then print insure_price
```

## 4.1 If-else branches — elif chain

Chain more conditions with elif when two branches are not enough. Python
checks each expression in order and stops at the first one that is True. The
note's anniversary gift example prints 'Newlyweds' for 1 year, 'Silver' for
25, 'Golden' for 50, and 'Congrats' for anything else.

```python
num_years = 50

# TODO: write that same if/elif/else chain for num_years and print the
#       matching message
```

## 4.2 Detecting equal values

The `==` operator checks whether two values are equal, without changing
either one the way a single `=` would.

```python
user_num = 17
div_remainder = user_num % 2

# TODO: use == to check whether div_remainder is 0, and print a message
#       saying whether user_num is even or odd
```

## 4.3 Detecting ranges (general)

When branches increase with no gaps, each elif only needs to state the top
of its range — the bottom is already implied by every branch above it having
been False.

```python
age = 11

# TODO: write an if/elif/else chain that prints 'No teams' for ages under 6,
#       'U8' for ages under 8, 'U10' for ages under 10, 'U12' for ages under
#       12, and 'No teams' for anything else
```

## 4.4 Relational operators

`<`, `>`, `<=`, and `>=` compare how one value relates to another.

```python
user_age = 32

# TODO: write an if/elif/else chain that sets insurance_price to 4800 if
#       user_age is under 25, 2350 if under 40, and 2100 otherwise, then
#       print insurance_price
```

## 4.4 Relational operators — chaining

Python lets you chain comparisons the way a mathematician would: `a < b < c`
checks both neighboring pairs at once.

```python
x = 12

# TODO: using a single chained comparison, check whether x sits strictly
#       between 10 and 15, and print the result
```

## 4.5 Logical operators

`and` requires both sides to be True, `or` requires at least one side to be
True, and `not` flips a single True/False value.

```python
user_channel = 250

# TODO: write an if/elif/else chain using and that sets channel_type to
#       'standard' for channels 2 through 499, 'hd' for channels 1002
#       through 1499, and 'error' otherwise, then print channel_type
```

## 4.6 Ranges with gaps

Some ranges have a gap in the middle that gets swallowed by an else — a
movie theatre discounts children 12 and under and seniors 65 and up, and
charges everyone else full price.

```python
user_age = 45

# TODO: write an if/elif/else chain that sets movie_ticket_price to 11 for
#       ages 12 and under, 12 for ages 65 and up, and 14 otherwise, then
#       print movie_ticket_price
```

## 4.7 Multiple features — separate ifs

Separate if statements are independent — each one is checked, and more than
one can run.

```python
balance = 5000
years = 8

# TODO: write two separate if statements: one that prints 'Premium' when
#       balance is greater than 1000, and one that prints 'Loyal' when
#       years is greater than 5
```

## 4.7 Multiple features — nested if-else

A nested if-else lives inside another branch's block, so the inner check
only happens once the outer condition has already been met.

```python
sales_type = 2
sales_bonus = 3

# TODO: write a nested if-else matching the note's bonus example: when
#       sales_type is 2, set sales_bonus to 10 if it is under 5, otherwise
#       add 2 to it; when sales_type is anything else, add 1 to sales_bonus.
#       Print sales_bonus at the end
```

## 4.8 Comparing data types

Strings compare character by character, and `==` treats different case as a
different string entirely.

```python
my_str = 'Friday'

# TODO: print the result of comparing my_str to 'Friday' with ==, and the
#       result of comparing my_str to 'friday' with ==
```

## 4.9 Membership and identity — in / not in

`in` and `not in` check whether a value shows up inside a container, such as
a list.

```python
roster = ['Alves', 'Messi', 'Fabregas']
name = 'Fabregas'

# TODO: use in to check whether name is on the roster, and print a message
#       saying whether it was found
```

## 4.9 Membership and identity — dictionaries check keys

Membership on a dictionary only looks at its keys, never its values.

```python
my_dict = {'A': 1, 'B': 2, 'C': 3}

# TODO: print whether 'B' is in my_dict, and print whether 2 is in my_dict
```

## 4.9 Membership and identity — is / is not

`is` checks whether two names are bound to the very same object, which is a
different question than `==` asking whether they hold the same value.

```python
w = 500
x = 500 + 500
y = w + w

# TODO: print the result of x == y, and print the result of x is y
```

## 4.10 Order of evaluation

Arithmetic happens before comparison, and comparison happens before the
logical operators — so without parentheses, an expression can evaluate in an
order that is easy to misread.

```python
member = False
age = 30

print(not member and age > 25)

# TODO: rewrite the expression above with explicit parentheses that show
#       the order Python actually evaluates it in, based on the precedence
#       rules, store it in a new variable, print it, and confirm it matches
#       the original line's output
```

## 4.11 Code blocks and indentation

Python decides what belongs to a branch purely from indentation, so nesting
one if-else inside another means nesting one indent level inside another.

```python
model = 'Toyota'
year = 1965
antique = False

# TODO: using nested if statements and correct indentation, set antique to
#       True when year is less than 1970, then, only when antique is True,
#       print 'Domestic antique.' if model is in ['Ford', 'Chevrolet',
#       'Dodge', 'Toyota']
```

## 4.12 Conditional expressions

A conditional expression takes the form `expr_when_true if condition else
expr_when_false` — a whole if-else squeezed onto one line when all it does
is choose a value.

```python
order_total = 75

# TODO: write a one-line conditional expression that sets shipping to 0 if
#       order_total is greater than 50, and 7 otherwise, then print shipping
```

Nice work — that covers every way this chapter branches. Loops are next.

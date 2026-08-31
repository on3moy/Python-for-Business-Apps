# Chapter 2: Variables, Objects, and Numbers

Practice assigning variables, naming them legally, inspecting objects, and working with Python's numeric, math, random, and text tools.

## 2.1 Variables and assignments

A variable is a name bound to a value with `=`. The name always goes on the
left, then `=`, then the value (`x = 13`, `JohnDoe = 55`).

```python
# TODO: create a variable named `hourly_rate` and assign it the value 24.50
```

## 2.2 Identifiers

An identifier is a legal Python name: letters, digits, and underscores,
starting with a letter or underscore, and case sensitive. The course default
naming style is `lower_case_with_underscores`.

```python
# TODO: create a variable that stores a customer's total number of orders.
#       Use a legal identifier written in lower_case_with_underscores style.
```

## 2.3 Objects

Every value in Python is an object with three properties: a **value**, a
**type**, and an **identity**. `print()`, `type()`, and `id()` are all
built-in functions that show you one of the three.

```python
x = '🦖'
print(x)

# TODO: print the type of x, then print the identity (id) of x
```

## 2.4 Numeric types

`float()` and `int()` convert a value to a floating-point number or an
integer, if the conversion is possible.

```python
price_text = '19.99'

# TODO: convert price_text to a float and print the result
```

## 2.5 Arithmetic expressions

Python follows the same order of operations you know from algebra:
parentheses, then exponents, then unary minus, then `*` `/` `%`, then `+`
`-`, evaluated left to right.

```python
shirt_price = 12
shipping_fee = 5
quantity = 3

# TODO: compute the total cost of buying `quantity` shirts, including the flat
#       shipping_fee, and store it in a variable named total_cost. Rely on
#       Python's order of operations rather than wrapping everything in
#       parentheses.
```

## 2.6 Compound operators

A compound operator combines an arithmetic operator with `=` as shorthand for
"take the variable, do the operation, and assign the result back to itself."
`age += 1` means the same thing as `age = age + 1`; the same pattern works for
`-=`, `*=`, `/=`, and `%=`.

```python
invoice_total = 100

# TODO: use a compound operator to apply a $15 late fee to invoice_total,
#       updating invoice_total in place rather than writing
#       invoice_total = invoice_total + 15
```

## 2.7 Division and modulo

Regular division (`/`) always returns a float. Floor division (`//`) rounds
that result down to the nearest whole number. Modulo (`%`) returns the
remainder left over from the division.

```python
invoice_count = 47
team_size = 5

# TODO: use floor division to find how many invoices each team member gets
#       evenly, storing the result in invoices_each. Then use modulo to find
#       how many invoices are left over, storing the result in
#       invoices_left_over.
```

## 2.8 Module basics

A module is a file containing Python code that other files can reuse. You
make a module's contents available with an `import` statement, and once it's
imported, you reach into whatever it defines using dot notation —
`module_name.thing_inside_it`.

```python
# TODO: import the math module, then use dot notation to print math.pi
```

## 2.9 Math module

The built-in `math` module has functions like `math.sqrt()` beyond basic
arithmetic. Once imported, dot notation reaches into whatever the module
defines.

```python
import math

num = 144
sqrt_num = math.sqrt(num)
print(sqrt_num)

# TODO: use a different function from the math module's table in the notes
#       to compute the factorial of 5, and print the result
```

## 2.10 Random numbers

`random.randint(min, max)` returns a random integer between `min` and `max`,
**inclusive** of both ends. `random.randrange(min, max)` is the same idea but
excludes `max`.

```python
import random

# TODO: simulate rolling a six-sided die by generating a random integer
#       between 1 and 6, inclusive, and print the result
```

## 2.11 Representing text — chr() and ord()

`chr()` converts a number (a Unicode code point) into its character. `ord()`
does the reverse, converting a character back into its number.

```python
num = 65

# TODO: use chr() to convert num into its character, then use ord() on that
#       character to convert it back into a number. Print both results.
```

## 2.11 Representing text — escape sequences

An escape sequence starts with a backslash and tells Python to do something
other than print the next character literally — `\n` for a newline, `\t` for
a tab, `\\` for a literal backslash, `\'` for a literal single quote.

```python
# TODO: write a single print() statement that outputs the text below across
#       two lines, using an escape sequence rather than two separate
#       print() calls:
#       Invoice #4521
#       Status: Paid
```

Nice work — that's every core building block from chapter 2. Chapter 3 builds strings, lists, tuples, and dictionaries on top of these.

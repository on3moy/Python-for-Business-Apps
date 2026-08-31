# Chapter 3: Strings, Lists, Tuples, and Dictionaries

Practice building and slicing the container types you'll lean on constantly in data work: strings, lists, tuples, and dictionaries.

## 3.1 String Basics — length

A string is a sequence of characters stored in a variable. `len()` is a
built-in function that returns how many characters are in a string.

```python
company_name = 'Acme Consulting'

# TODO: print the length of company_name using len()
```

## 3.1 String Basics — slicing

Slicing with `[]` lets you cut a piece out of a string using indexes.
Indexing always starts at 0, and the end of a range is exclusive — to grab
indexes 0 through 5 you slice `[:6]`, not `[:5]`.

```python
ticker = 'wowmom'

first_three = ticker[:3]
print(first_three)

# TODO: use slicing to grab the last three characters of ticker ('mom')
#       and print the result
```

## 3.1 String Basics — immutability

Strings are immutable — once created, a character inside a string cannot be
changed in place. `alphabet[0] = 'A'` raises an error. To change a string
you build a new one instead, for example by slicing out the part you want
to keep and concatenating it with `+`.

```python
invoice_id = 'inv-1001'

# TODO: without assigning to any character of invoice_id directly (that
#       would raise an error), use slicing and + to build a new string
#       that replaces the 'inv' prefix with 'INV', and print it
```

## 3.2 List Basics — creating and indexing

A list is a container created by surrounding a sequence of variables or
literals with `[]`. Each item is an **element**, and elements are ordered by
position — their **index** — starting at 0.

```python
prices = [19.99, 24.50, 8.75, 42.00]

# TODO: print the element at index 2 of prices
```

## 3.2 List Basics — append()

`+` concatenates two lists into a brand-new list, leaving the originals
untouched:

```python
x = [1, 2]
y = [3, 4]
combined = x + y
print(combined)
```

`append()` instead changes a list in place, adding one element at a time
without needing a new assignment.

```python
cart = ['pen', 'notebook']

# TODO: use append() to add 'stapler' to cart, then print cart
```

## 3.2 List Basics — pop() and remove()

`pop()` removes (and returns) the last element of a list by default.
`remove()` deletes an element by its value instead of its position.

```python
queue = ['Alex', 'Priya', 'Sam']

# TODO: use pop() to remove the last name from queue, storing the removed
#       name in a variable called last_in_line, then print both queue and
#       last_in_line
```

## 3.2 List Basics — modifying by index

You can also modify a list by assigning directly to an index, replacing
whatever element was there.

```python
scores = [88, 91, 76]

# TODO: replace the element at index 0 of scores with 95, then print scores
```

## 3.2 List Basics — sequence type functions

Lists support several of the same built-in functions numbers do:
`len(list)`, `min(list)`, `max(list)`, `sum(list)`, `list.index(val)`, and
`list.count(val)`.

```python
units_sold = [12, 45, 45, 3, 20]

# TODO: print the total of units_sold using sum(), then print how many
#       times 45 appears in units_sold using .count()
```

## 3.3 Tuple Basics

A tuple stores a collection of data, like a list, but is **immutable** —
once created, its elements cannot be changed. Use a tuple for values that
should stay fixed for everyone, like weekday names or category labels.

```python
weekdays = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri')

# TODO: print weekdays[0], then write a second line that tries to
#       reassign weekdays[0] to 'Monday' — run the cell and confirm Python
#       raises an error, then comment that second line back out
```

## 3.4 Dictionary Basics — creating a dictionary

A dictionary stores key:value pairs inside curly braces `{}`. Don't
confuse it with a `set()`, which also uses `{}` but holds plain comma
separated values with no colons — `{}` alone is an empty dictionary, not an
empty set.

```python
# TODO: create a dictionary named menu with at least two key:value pairs,
#       where each key is a menu item name (a string) and each value is
#       its price (a number)
```

## 3.4 Dictionary Basics — adding and deleting

Add a new key by assigning to it, `beans['black beans'] = ...`. Delete an
existing key with `del beans['professor']`.

```python
inventory = {'pens': 40, 'notebooks': 15}

# TODO: add a new key 'staplers' with a value of 8 to inventory, then
#       delete the 'pens' key from inventory, then print inventory
```

## 3.4 Dictionary Basics — reading from a dictionary

Grab one value with `beans['student']`. `.keys()`, `.values()`, and
`.items()` return all the keys, all the values, and all the key/value pairs.

```python
beans = {
    'professor': 'Moy'
    ,'student': 'Stephanie'
}

# TODO: print the value stored under 'student', then print beans.keys()
#       and beans.items()
```

## 3.10 String Formatting

An f-string is a string literal with an `f` right before the opening quote.
Anything inside `{}` gets evaluated and filled in, in order, left to right.

```python
# Old way: .format()
student = 'John Doe'
color = 'purple'
print('Hi my name is {}. {} is my favorite color'.format(student, color))

years = 21

# TODO: using an f-string, print "I am 21 years old." by filling in the
#       years variable
```

Nice work — that's every core building block from chapter 3. Chapter 4 puts these together with control flow.

# Python Crash Course
Note - This is not a comprehensive overview, you will need to review Python or take a course on it. Think of this notebook as the "cram session" version of everything IS 640 covers — we're gonna move fast, crack some jokes, and get you comfortable enough to read and write real business Python. Lets go. 🦖

# Topics Covered

## Data Types
- Strings
- Integers
- Lists
- Dictionaries
- Booleans
- Tuples
- Sets

## Other Topics
- Operators
- If, else, elif
- Loops
- While loops
- Range()
- enumerate() and zip()
- List comprehension
- Dictionary comprehension
- sorted() with a key
- Tuple/multiple assignment unpacking
- Number formatting (currency, percentages)
- A couple of classic beginner gotchas
- Functions
- Methods
- Lambda expressions
- Map and filters

# Data Types

Everything in Python is a value with a type attached to it, and numbers are the easiest place to start because you already know the rules — this is just the arithmetic you learned in like 3rd grade, except now a computer does it for you at Excel-spreadsheet speed. If you've ever built a formula in Excel (`=B2*C2+D2`), you already have the right mental model. Lets warm up with some basic math so Python doesn't feel scary.

```python
# Addition
1 + 0
```

```python
# Multiplication
1 * 0
```

Division in Python always gives you back a float (a decimal), even if the math works out evenly. This trips people up constantly, so keep it in the back of your mind.

```python
# Division
0 / 1
```

```python
# Floor Division - this rounds DOWN to the nearest whole number, no decimals allowed
5 // 2
```

```python
# Exponential - because sometimes you need to raise something to a power, like compound interest
2 ** 4
```

Modulo (`%`) gives you the *remainder* after division. This one seems useless until the day you need it to figure out if a number is even/odd, or to split a big list of customers into even batches — then it becomes your best friend.

```python
# Modulo Example 1
4 % 2
```

```python
# Modulo Example 2
5 % 2
```

Python respects order of operations (PEMDAS), just like Excel and just like your algebra teacher drilled into you.

```python
# Order of Operations
(1 + 3) * (2  + 2)
```

# Variables

A variable is just a name you're giving to a value so you can reuse it later instead of retyping it a million times. Think of it like a labeled cell in Excel — except instead of `B2`, you get to pick the name yourself. Lets make one named after your favorite instructor. 😉

```python
moy = 13
```

```python
x = 1
y = 2
```

```python
z = x + y + moy
```

```python
z
```

# Strings

Strings are just text, and Python is chill about how you wrap it — single quotes or double quotes both work, they just need to match on both ends.

```python
'Single Quotes'
```

```python
"Double Quotes"
```

Here's the one case where the quote style actually matters — if your text has an apostrophe in it, wrapping it in double quotes saves you from having to escape anything.

```python
"I don't want to review python"
```

# Prints

`print()` is how you tell Python "hey, show this to the human." It might seem redundant right now in a notebook (since a cell shows its last line automatically), but the second you start writing real scripts and automations, `print()` is the only way anything shows up at all.

```python
mo = 'WOW'
```

```python
mo
```

```python
print(mo)
```

```python
number = 100
name = 'Goku'
```

There's an old-school way to build strings with placeholders using `.format()`, and then there's the way you should actually use in 2026: f-strings. Lets see both so you recognize the old style when you inherit someone else's code.

```python
# Formats
print('I can count up to {something1} before {something2} does kamehameha'.format(something1=number, something2=name))
```

```python
# Format ex. 2
print('I can count up to {} before {} does kamehameha'.format(number, name))
```

```python
# F string - just slap an f in front of the quotes and drop your variables in {}
print(f'{name} is older than {number}')
```

## Number Formatting (because nobody wants to see `1439.9999999997` on an invoice)

This is where f-strings earn their keep in a business context. You can format a number's decimals, add comma thousands-separators, and even turn a decimal into a percentage — all *inside* the `{}`. This is the exact trick you'll want for salary numbers, invoice totals, and tax rates so your reports don't look like they came out of a calculator's receipt tape.

```python
salary = 84250.5
tax_rate = 0.223

# :,.2f means "comma-separate the thousands, show exactly 2 decimal places"
print(f'Annual salary: ${salary:,.2f}')

# :.1% turns a decimal into a percentage for you, decimal point and all
print(f'Effective tax rate: {tax_rate:.1%}')
```

```python
# Did you notice the only way to bring data into an f-string is by using {}?
# And that the formatting spec (the stuff after the colon) is optional?
invoice_total = 1439.999999997
print(f'Invoice total (ugly): {invoice_total}')
print(f'Invoice total (professional): ${invoice_total:,.2f}')
```

# Lists

A list is an ordered, changeable collection of stuff, wrapped in `[]`. If a dictionary is like a labeled Excel cell, a list is basically a whole column — order matters and you can have duplicates.

```python
# A list has []
[1, 2, 3]
```

```python
['moy', name, ['a',2, number]]
```

```python
popo_list = ['a', 'b', 'c', ['more', 'nested', 'stuff']]
```

Indexing starts at 0, not 1 — this trips up literally every beginner at some point, so don't feel bad when it gets you too.

```python
popo_list[3]
```

```python
popo_list[0]
```

Slicing lets you grab a chunk of the list instead of a single item — `[start:stop]`, and leaving either side blank means "go all the way to that end."

```python
popo_list[1:]
```

```python
popo_list[:2]
```

```python
popo_list[:-1]
```

Lists are mutable, meaning you can reach in and change an item after the fact.

```python
popo_list[0] = 13
popo_list
```

```python
popo_list[3][2]
```

# Dictionaries

Dictionaries store data as `key: value` pairs instead of by position. Dictionaries are versatile and highly used in my data analytics experience! Get to know how to use dictionaries! Think of a dictionary as a single row of data where every column has a label — way closer to how a real invoice or a database record actually looks than a plain list is.

```python
dic1 = {'key': 'value', 'key2': 'value2'}
```

```python
dic1['key2']
```

```python
dic1.keys()
```

```python
dic1.values()
```

```python
dic1.items()
```

# Tuples

A tuple looks like a list but uses `()` instead of `[]`, and the big difference is tuples are **immutable** — once you make one, you can't change it. Use these when you have a fixed set of values that should never accidentally get edited, like coordinates or a (month, year) pair.

```python
tuple1 = (1, 2, 3, 4, 5, 5)
```

```python
tuple1[3]
```

```python
try:
    tuple1[3] = 'Hola'
except Exception as e:
    print(type(e).__name__)
    print(type(e).__doc__)
    print(e)
```

## Multiple assignment (tuple unpacking)

Here's a genuinely handy trick — Python lets you assign several variables in one line by unpacking a tuple (or any sequence) straight into names. You'll see this constantly with `.items()` on a dictionary, or when a function hands you back more than one value.

```python
# Unpack a tuple into three separate variables in one shot
employee = ('Moy', 'Analyst', 84250.5)
first_name, role, pay = employee

print(first_name)
print(role)
print(pay)
```

```python
# The classic use case: looping over dic1.items() and unpacking key/value at once
for key, value in dic1.items():
    print(f'{key} -> {value}')
```

```python
# You can even swap two variables without a temp variable - this one always
# blows people's minds coming from other languages
a, b = 1, 2
a, b = b, a
print(a, b)
```

# Sets

A set is an *unordered* collection with zero tolerance for duplicates — feed it the same value twice and it just quietly drops one. Great for "give me only the unique values" type problems.

```python
set1 = {1, 2, 3, 4, 5, 5}
```

```python
set1
```

Sets don't support indexing — there's no "first item" because there's no guaranteed order in the first place.

```python
try:
    set1[0] = 13
except Exception as e:
    print(type(e).__name__)
    print(type(e).__doc__)
    print(e)
```

# Operators

Comparison operators ask Python a yes/no question and hand you back a boolean (`True` or `False`). These are the building blocks of every `if` statement you'll ever write.

```python
4 > 2
```

```python
0 >= 2
```

```python
0 == 1
```

Strings are compared character by character, and whitespace absolutely counts — 'Goku' and 'Goku ' are NOT the same string, even though your eyes might not catch the trailing space.

```python
'Goku' == 'Goku '
```

```python
'Goku' == 'Goku'
```

## Logic Operators

`and` requires both sides to be true, `or` only needs one.

```python
(2 > 0) and (3 > 5)
```

```python
(2 > 0) or (3 > 5)
```

# If, elif, else Statements

Conditionals are how your program makes decisions — this is the "if this happens, do that" logic that's basically an Excel `IF()` formula, except you can chain as many conditions together as you want.

```python
if 3 > 4:
    print('Print if statement is true')
else:
    print('Print if statement is false')
```

```python
if 3 < 4:
    print('Print if statement is true')
else:
    print('Print if statement is false')
```

`elif` lets you check more conditions if the first one fails, without nesting a bunch of nested `if` statements inside each other.

```python
if 1 > 2:
    print('First Statement')
elif 13 == 13:
    print('Middle Statement')
else:
    print('Last Statement')
```

# For Loop

A `for` loop lets you walk through a collection item by item and do something with each one, instead of writing the same line of code 500 times for 500 rows of data. This is the whole reason automation beats doing things by hand in Excel.

```python
a_list = ['I', 'am', 'one', 'or', 1]
```

```python
for something in a_list:
    print(something)
```

You don't have to name your loop variable something meaningful — `_` is a common convention for "I'm not actually going to use this variable, I just need to loop N times."

```python
for _ in a_list:
    print(_)
    print('repeat this')
```

`range()` generates a sequence of numbers for you on the fly, without you having to type them all out.

```python
for x in range(5):
    print(x)
```

```python
list(range(5))
```

## enumerate() and zip()

Two loop helpers you will use constantly once you know they exist. `enumerate()` hands you back the index *and* the value at the same time, so you never have to manually keep a counter variable. Perfect for numbering invoice line items 1, 2, 3... instead of starting at index 0 like a robot.

```python
line_items = ['Consulting hours', 'Software license', 'Support retainer']

for i, item in enumerate(line_items, start=1):
    print(f'{i}. {item}')
```

`zip()` lets you walk through two (or more) lists side by side, pairing them up position by position — great for lining up a list of product names with a parallel list of prices.

```python
products = ['Widget', 'Gadget', 'Doohickey']
prices = [19.99, 34.50, 12.00]

for product, price in zip(products, prices):
    print(f'{product}: ${price:,.2f}')
```

# While Loops

A `while` loop keeps running as long as its condition stays true. Unlike a `for` loop, you're on the hook for making sure the condition eventually becomes false — forget to update your counter and you've got yourself an infinite loop and a very unhappy laptop fan.

```python
i = 1
while i < 5:
    print(f'i = {i}')
    i += 1
```

# List Comprehension

A list comprehension is a one-line shortcut for the classic "make an empty list, loop over something, `.append()` to it" pattern. It's more compact and honestly once it clicks, more readable too.

```python
numberList = [1, 2, 3, 4, 5]
inputList = []
for element in numberList:
    inputList.append(element**2)
print(inputList)
```

```python
# Same result, one line - this is the comprehension version of the loop above
[x**2 for x in numberList]
```

## Dictionary Comprehension

Same idea as a list comprehension, but you build a dictionary instead — `{key_expr: value_expr for item in iterable}`. Super handy for reshaping data, like turning a list of employee names into a dictionary that maps each name to their name length, or (more realistically) mapping product names to prices.

```python
# Build a dict mapping each product to its price, doubled - Black Friday markup gag, not real advice
products_prices = {'Widget': 19.99, 'Gadget': 34.50, 'Doohickey': 12.00}

marked_up = {product: round(price * 1.5, 2) for product, price in products_prices.items()}
marked_up
```

```python
# You can filter inside a comprehension too - only keep products under $20
cheap_stuff = {product: price for product, price in products_prices.items() if price < 20}
cheap_stuff
```

## sorted() with a key

`sorted()` gives you back a sorted copy of a list. On its own it just sorts numbers or strings the obvious way, but the real power move is the `key=` argument — you hand it a function that says "sort by *this* instead," which is exactly what you need when you're sorting a list of dictionaries by one of their fields (like sorting invoice line items by total, highest to lowest).

```python
numbers = [5, 2, 9, 1, 5]
sorted(numbers)
```

```python
# reverse=True flips it to descending order
sorted(numbers, reverse=True)
```

```python
# key= takes a function - here we use a lambda (more on those later) to say
# "sort by the 'total' field of each dictionary"
invoice_items = [
    {'item': 'Consulting hours', 'total': 1200.00},
    {'item': 'Software license', 'total': 499.99},
    {'item': 'Support retainer', 'total': 2500.00},
]

sorted(invoice_items, key=lambda row: row['total'], reverse=True)
```

# Business Example: Invoicing 🧾

Lets pull everything above together into one thing you'll actually do on the job: you've got a list of invoice line items (a list of dictionaries, basically a mini spreadsheet), and you need to add tax, format everything as currency, and rank the items by cost. This is the whole point of the course — turning "I can write `for` loops" into "I can process a business report."

```python
invoice = [
    {'item': 'Consulting hours', 'qty': 20, 'unit_price': 60.00},
    {'item': 'Software license', 'qty': 1, 'unit_price': 499.99},
    {'item': 'Support retainer', 'qty': 3, 'unit_price': 833.33},
]

TAX_RATE = 0.0725  # sales tax, shouting because it's basically a constant

# Dict comprehension to compute a subtotal per item
subtotals = {row['item']: round(row['qty'] * row['unit_price'], 2) for row in invoice}
subtotals
```

```python
# Now sort those line items biggest-to-smallest, so the boss sees the big
# ticket items first instead of scrolling for them
ranked = sorted(subtotals.items(), key=lambda pair: pair[1], reverse=True)

for item, subtotal in ranked:
    print(f'{item:<20} ${subtotal:>10,.2f}')
```

```python
# Grand total with tax applied, formatted like a real invoice instead of
# whatever ugly float Python wants to hand you
grand_total = sum(subtotals.values()) * (1 + TAX_RATE)
print(f'Grand total (incl. {TAX_RATE:.2%} tax): ${grand_total:,.2f}')
```

# Functions

A function is a reusable, named chunk of code — write the logic once, call it as many times as you want. Think of it like an Excel macro: you record the steps once, then reuse them forever without retyping.

```python
def my_func(param1='some default value'):
    '''
    DocString: Some documentation and details of how your func works.
    '''
    print(param1)
```

```python
my_func
```

```python
my_func()
```

```python
my_func('Not a default value, :)')
```

```python
def squarethis(number):
    return number**2
```

```python
squared_value = squarethis(4)
print(squared_value)
```

## A couple of classic beginner gotchas

Every Python programmer face-plants into these at least once, so lets get them out of the way now instead of you discovering them at 2am before a deadline.

**Gotcha #1: `==` vs `is`.** `==` asks "do these have the same *value*?" `is` asks "are these literally the exact same object in memory?" 99% of the time you want `==`. `is` is really only for comparing against `None`.

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # True - same values
print(a is b)  # False - two different list objects that happen to look alike
```

**Gotcha #2: mutable default arguments.** If you use an empty list (or dict) as a default argument, Python only creates that list ONE time, ever — not fresh on every call. Every call that relies on the default ends up sharing (and mutating!) the *same* list. This one has bitten every Python dev at least once.

```python
def add_item(item, cart=[]):  # DANGER: don't do this in real code
    cart.append(item)
    return cart

print(add_item('apple'))
print(add_item('banana'))  # you'd expect just ['banana'], but nope
```

```python
# The fix: default to None, and create a fresh list INSIDE the function
def add_item_safely(item, cart=None):
    if cart is None:
        cart = []
    cart.append(item)
    return cart

print(add_item_safely('apple'))
print(add_item_safely('banana'))  # now it behaves like you'd expect
```

# Methods

Methods are functions that belong to an object and act on that object directly — you call them with dot notation, `object.method()`. Strings come loaded with a ton of useful built-in methods.

```python
stringy = 'Hi, my name is Harry. Harry Potter.'
```

```python
stringy.lower()
```

```python
stringy.upper()
```

```python
stringy.split()
```

```python
stringy.split('.')
```

```python
stringy.split('.')[0]
```

# Lambda Expresssions

A lambda is a tiny, throwaway, unnamed function — good for one-line logic you're only going to use once (like inside `sorted(..., key=...)` above), not for anything complicated enough to need a docstring.

```python
def replaceMe(something):
    return something + 10
```

```python
replaceMe(5)
```

```python
# Same logic as replaceMe, but as a lambda - no def, no name, no return keyword
lambda x : x + 10
```

# Map and Filters

`map()` applies a function to every item in a collection, and `filter()` keeps only the items that pass a test — both return a lazy iterator, so you usually wrap them in `list()` to actually see the results.

```python
aList = [1, 2, 3, 4, 5]
```

```python
map(replaceMe, aList)
```

```python
list(map(replaceMe, aList))
```

```python
list(map(lambda x : x + 10, aList))
```

```python
filter(lambda element : element % 2 == 0, aList)
```

```python
list(filter(lambda element : element % 2 == 0, aList))
```

That's the crash course! You now know enough Python to be dangerous — go build something, break it, google the error message, fix it, and repeat. That loop right there (not the `for` kind) is basically the entire job. 🦖

# Great Job!
![Great Job!](https://i0.wp.com/michelleismoneyhungry.com/wp-content/uploads/2013/07/gatsby-leo-051113.gif?resize=500%2C239&ssl=1)

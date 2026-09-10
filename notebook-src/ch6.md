# Chapter 6: Functions

Practice writing your own functions — defining them, calling them, and using the tools Python gives you to control their inputs, outputs, and scope.

## 6.1 User-defined function basics — defining and calling

A function definition is the `def` line plus its indented body; a function call is the name followed by `()`. A parameter is a named input listed in the definition, and the value handed to it at call time is the argument.

```python
weight_lb = 150

# TODO: define a function named lb_to_kg that takes a weight in pounds as a
#       parameter and returns the equivalent weight in kilograms, using
#       0.453592 kilograms per pound, then call it with weight_lb and print
#       the result
```

## 6.1 User-defined function basics — calling one function from another

A function's own statements can call other functions, the same way `int(input())` feeds one function's result straight into another.

```python
def double(n):
    return n * 2

# TODO: define a function named quadruple that takes a number and returns
#       four times that number, but instead of multiplying by 4 directly,
#       have it get there by calling double() twice
```

## 6.2 Print functions

A void function has no `return` statement — it still hands back `None`, but nobody uses that value. It has a job (usually printing) and does it.

```python
name1, qty1, price1 = 'Ravi', 3, 12.50
name2, qty2, price2 = 'Ana', 1, 40.00

# TODO: define a void function named print_receipt that takes a customer
#       name, a quantity, and a unit price, and prints two lines: the
#       customer's name, then 'Qty: {quantity} @ ${price:.2f}' -- then call
#       it once for each customer above
```

## 6.3 Dynamic typing

Python never checks a parameter's type ahead of time, which is exactly what lets the same function behave differently depending on what type it's handed — that's polymorphism.

```python
def combine(x, y):
    return x + y

# TODO: call combine() once with two integers, then call it again with two
#       strings, printing both results to see the same function behave two
#       different ways
```

## 6.4 Reasons for defining functions

Spotting the same calculation typed out more than once is the clearest sign a function belongs there instead.

```python
sales1 = 1200
sales2 = 800
sales3 = 3000

# TODO: define a function named calc_commission that takes a sales amount
#       and returns 5% of it, then use it to compute and print a commission
#       for each of sales1, sales2, and sales3
```

## 6.5 Writing mathematical functions — function calls inside expressions

A function call evaluates to whatever it returns, so it can be dropped directly into a larger expression, the same way a variable can.

```python
def cube(n):
    return n ** 3

# TODO: using cube(), write a single expression that adds cube(3) and
#       cube(4) together and print the result
```

## 6.5 Writing mathematical functions — modular math functions

A bigger mathematical function can lean on a smaller one instead of reinventing it.

```python
def calc_rectangle_area(width, height):
    return width * height

# TODO: define a function named calc_box_volume that takes a width, a
#       height, and a depth, and returns the box's volume by calling
#       calc_rectangle_area() for the base and multiplying that by depth --
#       then call it with numbers of your choice and print the result
```

## 6.6 Function stubs

A function stub is a definition whose body isn't finished yet — just enough to satisfy Python's rule that a function body can't be empty, so the rest of the program can be tested while that piece is still being written.

```python
def steps_to_miles(steps):
    return steps / 2000

print(steps_to_miles(8000))

# TODO: below this, add a stub for a function named steps_to_active_minutes
#       that will eventually estimate active minutes from a step count --
#       it doesn't need to compute anything yet, just be a valid, empty
#       function body
```

## 6.7 Functions with branches/loops

If/elif/else and loops work exactly the same inside a function body as they do in the main program.

```python
# TODO: define a function named calc_shipping_cost that takes a package
#       weight in pounds and returns its cost: $5 flat if the weight is 2
#       pounds or less; $5 plus $1.50 per pound over 2 if the weight is 20
#       pounds or less; and $5 plus $1.50 per pound for the first 18 pounds
#       over 2, plus $3 per pound beyond that, otherwise -- then call it
#       with a weight of your choice and print the result
```

## 6.8 Functions are objects — assigning a function to a variable

`def` creates an actual function object, and a name can be bound to that object without calling it — no parentheses means nothing runs yet.

```python
def print_dog():
    print('woof')

# TODO: create a new variable named alias that refers to the print_dog
#       function itself (not a call), then call the function through alias
```

## 6.8 Functions are objects — passing a function as an argument

Because a function is just an object, it can be handed to another function as an argument, which can then call it without knowing which one it received.

```python
def print_square_frame():
    print('[    ]')

def print_circle_frame():
    print('(    )')

def print_picture(frame):
    frame()
    print('  photo  ')

# TODO: call print_picture() twice -- once passing it print_square_frame,
#       and once passing it print_circle_frame
```

## 6.9 Functions: Common errors — copy-paste errors

Copying a function to build a similar one is a reasonable shortcut, right up until one leftover name from the original doesn't get updated.

```python
def miles_to_km(miles):
    result = miles * 1.60934
    return miles

print(miles_to_km(10))

# TODO: this function has a copy-paste bug like the one described in the
#       note -- find and fix the line so miles_to_km actually returns the
#       converted result instead of the original argument
```

## 6.9 Functions: Common errors — return errors

If execution reaches the end of a function without hitting a `return`, the function quietly hands back `None` — no traceback, just a silently wrong answer.

```python
def area_of_square(side):
    a = side * side

print(area_of_square(5))

# TODO: this function is missing its return statement, which is why it
#       prints None -- add the line needed so it returns the computed area
```

## 6.10 Scope of variables and functions — reading a global from inside a function

A global variable, created outside any function, is readable from inside a function with no extra syntax at all.

```python
tax_rate = 0.0725

# TODO: define a function named calc_total that takes a price, computes a
#       local variable equal to the price plus the price times tax_rate,
#       and returns it -- then call it with a price of your choice and
#       print the result
```

## 6.10 Scope of variables and functions — modifying a global from inside a function

Assigning to a global variable from inside a function needs an explicit `global` statement, or Python just creates a separate local variable with the same name instead.

```python
current_user = 'guest'

def log_in():
    # TODO: use the global keyword so that assigning to current_user inside
    #       this function updates the global variable, then set
    #       current_user to 'admin'
    pass

log_in()
print(f'Current user: {current_user}')
```

## 6.11 Namespaces and scope resolution

A namespace is a mapping of names to objects, and `globals()` lets you look at the global namespace directly.

```python
print(globals())

# TODO: assign a new variable named favorite_language to a string of your
#       choice, then call globals() again and confirm your variable now
#       appears in the dictionary
```

## 6.12 Function arguments — immutable arguments

Python passes a reference to the same object, not a copy -- but rebinding an immutable argument inside a function never reaches back out to the caller.

```python
def increase(num):
    num = num + 1

original_score = 88

# TODO: call increase() with original_score, then print original_score to
#       see whether the immutable integer argument changed outside the
#       function
```

## 6.12 Function arguments — mutable arguments

A mutable object modified in place inside a function is visible everywhere else that same object is referenced, because no copy was ever made.

```python
def add_task(tasks):
    tasks.append('submit report')

my_tasks = ['email team']

# TODO: call add_task() with my_tasks, then print my_tasks to see whether
#       the mutable list argument changed outside the function
```

## 6.13 Keyword arguments and default parameter values — keyword arguments

A keyword argument matches a parameter by name instead of by position, so once every argument is passed this way, their order stops mattering.

```python
def print_invoice(client, amount, due_date):
    print(f'{client} owes ${amount} by {due_date}')

# TODO: call print_invoice() once using keyword arguments, listing the
#       arguments in a different order than the parameter list, and confirm
#       the output is still correct
```

## 6.13 Keyword arguments and default parameter values — default parameter values

A default parameter value is set in the function definition itself and is used automatically whenever the caller omits that argument.

```python
def print_greeting(name, formal=False):
    if formal:
        print(f'Good day, {name}.')
    else:
        print(f'Hey {name}!')

# TODO: call print_greeting() twice -- once passing only a name, so formal
#       uses its default, and once explicitly overriding formal to True
```

## 6.14 Arbitrary argument lists — \*args

A parameter prefixed with `*` collects any extra positional arguments into a tuple, however many the caller passes.

```python
def print_playlist(first_song, *args):
    print(f'Now playing: {first_song}')
    if len(args) > 0:
        print('Up next:', *args)

# TODO: call print_playlist() once with just one song title, then call it
#       again with a song title plus three more titles, to see how *args
#       collects the extras
```

## 6.14 Arbitrary argument lists — \*\*kwargs

A final parameter prefixed with `**` collects any extra keyword arguments into a dictionary, using the argument names as keys.

```python
def print_profile(username, **kwargs):
    print(f'User: {username}')
    for field, value in kwargs.items():
        print(f' {field}: {value}')

# TODO: call print_profile() with a username and two keyword arguments of
#       your choice (for example city and age), to see how **kwargs
#       collects them
```

## 6.15 Multiple function outputs

`return` still only ever hands back one value -- but that one value can be a tuple, which is how a function reports more than one thing at once.

```python
def get_order_totals(prices):
    subtotal = sum(prices)
    tax = subtotal * 0.08
    return subtotal, tax

# TODO: call get_order_totals() with a list of prices of your choice,
#       unpacking the returned tuple into two variables named subtotal and
#       tax, then print both
```

## 6.16 Docstrings — writing one

A docstring is a string literal placed as the very first line inside a function's body, describing what the function does.

```python
def calc_late_fee(days_late):
    return days_late * 2.50

# TODO: add a one-line docstring to calc_late_fee, right after the def
#       line, describing what it does
```

## 6.16 Docstrings — using help()

`help()` prints out whatever documentation is attached to an object -- for a function, that means its docstring plus its parameter list.

```python
# TODO: call help() on calc_late_fee to see its docstring and parameter
#       list printed out
```

## 6.17 Engineering examples — a global constant plus a one-line function

A physical or business constant that no function should ever modify is exactly the kind of value worth defining once, globally, outside of any function.

```python
annual_rate = 0.045

# TODO: define a function named simple_interest that takes a principal
#       amount and a number of years, and returns the interest earned using
#       interest = principal * annual_rate * years -- then call it with
#       numbers of your choice and print the result
```

## 6.17 Engineering examples — multiple outputs from a formula

Combining a global constant, a function, and a tuple return brings together several tools from this chapter at once.

```python
def temp_conversions(fahrenheit):
    pass

# TODO: replace the pass above so the function returns both the Celsius
#       and Kelvin equivalents of fahrenheit as a tuple, using
#       celsius = (fahrenheit - 32) * 5 / 9 and kelvin = celsius + 273.15
#       -- then call it with a Fahrenheit value of your choice, unpacking
#       the result into two variables and printing both
```

Nice work -- that covers every function tool this chapter introduced.

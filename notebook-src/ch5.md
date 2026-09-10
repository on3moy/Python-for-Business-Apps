# Chapter 5: Loops

Practice writing while loops, for loops, and the tools that control what they do along the way.

## 5.1 Loops (general)

A loop's condition only ever changes if something inside the loop body updates
the variable it depends on. The general shape is always the same: initialize
a variable before the loop, update it inside the loop, and read the final
answer only after the loop ends.

```python
values = [5, 3, 8, 0, 2]
index = 0
val = values[index]
total = 0

# TODO: write a while loop that keeps adding val to total for as long as val
#       is not 0, moving index forward and pulling the next entry from
#       values into val on every pass, then print total once the loop ends
```

## 5.2 While loops — basic while loop

A while loop keeps running its body for as long as its condition stays True,
checking the condition again before every single pass.

```python
level = 1

# TODO: write a while loop that prints level and then triples it,
#       continuing for as long as level is less than 50, then print 'Done'
#       once the loop has ended
```

## 5.2 While loops — sentinel values

A sentinel value exists purely to signal "stop the loop" — it is not real
data, it is a flag the loop's condition is watching for.

```python
correct_word = 'star'
guesses = ['nova', 'comet', 'star', 'moon']
index = 0
guess = guesses[index]

# TODO: write a while loop that keeps moving to the next guess in guesses
#       for as long as guess does not equal correct_word, then print
#       'Access granted.' once the loop ends
```

## 5.3 More while loop examples — peeling off digits

`%` and `//` together let you pull a number apart one digit at a time,
starting from the rightmost digit.

```python
num = 4517

# TODO: write a while loop that prints one digit of num at a time, from the
#       rightmost digit to the leftmost, using % and // the way the note's
#       example does
```

## 5.3 More while loop examples — greatest common divisor

Euclid's algorithm finds a GCD by repeatedly subtracting the smaller value
from the larger one until the two values are equal.

```python
num_a = 42
num_b = 18

# TODO: write a while loop implementing Euclid's algorithm, the same way
#       the note does, so that once the loop ends num_a holds the greatest
#       common divisor of the two starting values, then print num_a
```

## 5.3 More while loop examples — guarding a sentinel average

A sentinel-driven loop that computes an average needs a guard for the case
where nothing was ever entered before the sentinel showed up, or the
division crashes with a `ZeroDivisionError`.

```python
entries = [8, 12, 5, 0]
index = 0
val = entries[index]

values_sum = 0
num_values = 0

# TODO: write a while loop that sums entries into values_sum and counts
#       them in num_values for as long as val is not 0, moving to the next
#       entry on every pass, then print the average -- but only if
#       num_values is greater than 0, the way the note warns you to guard
#       against ZeroDivisionError
```

## 5.4 Counting — counting down

Nothing says a counting loop has to count up by 1 each time — decrement
instead, or step by any amount you like.

```python
balance = 40

# TODO: write a while loop that prints balance and then decreases it by 8
#       each pass, continuing for as long as balance is greater than or
#       equal to 0
```

## 5.4 Counting — a formula built from counting

A running factorial is just a counting loop with one extra line of math
tucked inside the body, using a compound operator to update the result.

```python
factorial = 6
count = factorial - 1

# TODO: write a while loop, the same shape as the note's factorial example,
#       that multiplies factorial by count each pass using *=, decreasing
#       count by 1 each time, continuing while count is at least 1, then
#       print the result
```

## 5.5 For loops — basic for loop

A for loop assigns a variable to the current element on every pass, and
stops on its own once every element has been visited — no condition to
write yourself.

```python
cities = ['Reno', 'Boise', 'Tacoma']

# TODO: write a for loop that prints a greeting for every city in cities,
#       the way the note's name example does, then print 'Done' after the
#       loop
```

## 5.5 For loops — iterating over strings and dictionaries

A string is a sequence, so a for loop walks it character by character. A
dictionary hands a for loop its keys, in insertion order — you look up the
value yourself.

```python
word = 'Loop'
channels = {'ESPN': 24, 'FOX': 11}

# TODO: write a for loop that prints each character in word, then a second
#       for loop that prints a sentence naming each channel and its number
#       by looking the value up from channels the way the note's example
#       does
```

## 5.5 For loops — running total

Walking a container with a for loop is the natural way to build up a
running total across every item.

```python
weekly_hours = [7.5, 8, 6.25, 9]

total = 0
# TODO: write a for loop that adds every value in weekly_hours into total,
#       then compute and print the average hours worked per day
```

## 5.5 For loops — looping backward with reversed()

`reversed()` flips the order a for loop walks through, without touching the
original container.

```python
runners = ['Diaz', 'Kim', 'Osei']

# TODO: use reversed() in a for loop to print runners from last to first,
#       each on the same line separated by a space
```

## 5.6 Counting using range() — basic range()

`range()` generates a sequence of integers without needing a container to
already exist. One argument means "start at 0, stop before this number."

```python
# TODO: use range() with a for loop to print the integers 0 through 6
```

## 5.6 Counting using range() — negative step

Give `range()` a negative step and it counts down instead of up.

```python
# TODO: use range() with a negative step inside a for loop to print
#       15, 12, 9, 6, 3, each separated by a space
```

## 5.6 Counting using range() — range() is not a list

`range()` produces its own sequence type, not a list — wrapping it in
`list()` is the only reason to see the values it would generate all at once.

```python
sequence = range(2, 20, 5)

# TODO: print sequence itself, then print it converted to a list with
#       list(), the way the note shows
```

## 5.7 While vs. for loops

Use a for loop whenever the number of iterations is knowable before the
loop starts — a for loop over `range()` is guaranteed to finish, with no
update line for you to forget.

```python
i = 0
while i < 8:
    print(i)
    i += 1

# TODO: rewrite the while loop above as an equivalent for loop using
#       range(), printing the same numbers
```

## 5.8 Nested loops — pairing items from two lists

For every single pass of the outer loop, the entire inner loop runs start
to finish — that is what generates every combination of two things.

```python
sizes = ['S', 'M', 'L']
colors = ['red', 'blue']

# TODO: write a nested for loop that prints every combination of a size and
#       a color, one per line, the way the note's domain-name example pairs
#       letters
```

## 5.8 Nested loops — building a grid

Nested for loops are the natural way to print anything shaped like rows and
columns — the outer loop picks the row, the inner loop fills that entire
row before the outer loop moves on.

```python
num_rows = 3
num_cols = 4

# TODO: write a nested for loop that prints a grid of '#' characters with
#       num_rows rows and num_cols columns, the way the note's example
#       builds a rectangle
```

## 5.9 Developing programs incrementally

Before adding any real logic to a loop, it is worth proving the loop
actually visits every element first — a small, throwaway version confirms
that much before anything else gets layered on top.

```python
word = 'PYTHON'

# TODO: write a for loop with a manual index counter that prints
#       'Element {index} is: {character}' for every character in word, the
#       same way the note's Version 1 step confirms a loop visits every
#       character
```

## 5.10 Break and continue — break

A `break` statement immediately exits the loop it is inside — no more
iterations, no matter what the loop's condition says.

```python
inventory = [12, 45, 8, 90, 3]
target = 90

# TODO: write a for loop over inventory that prints 'Found it' and uses
#       break to stop the loop as soon as it reaches target
```

## 5.10 Break and continue — continue

A `continue` statement immediately jumps back up to the loop's condition
check, skipping whatever is left of the current iteration's body.

```python
# TODO: write a for loop over range(30) that uses continue to skip any
#       number not divisible by 4, printing only the numbers that are
```

## 5.11 Loop else

A loop's `else` clause runs only if the loop finished all its iterations
normally — meaning nobody hit a `break` along the way.

```python
roster = ['Owens', 'Reid', 'Kato', 'Blake']
target_name = 'Reid'

# TODO: write a for loop over roster that breaks as soon as it finds
#       target_name, printing 'Found.' when it does, and attach an else
#       clause to the loop that prints 'Not found.' only when the loop
#       finishes without ever hitting break
```

## 5.12 Getting both index and value when looping: enumerate() — enumerate()

`enumerate()` wraps a container and yields an `(index, value)` pair on
every iteration, so a for loop can grab both without any manual bookkeeping.

```python
flights = ['DL200', 'UA88', 'AA15']

# TODO: use enumerate() in a for loop to print 'Flight {index}: {value}'
#       for every entry in flights
```

## 5.12 Getting both index and value when looping: enumerate() — unpacking

Unpacking assigns multiple variables from a single sequence in one line —
it is the same mechanism that lets a for loop grab both values out of each
`(index, value)` pair `enumerate()` hands back.

```python
coordinate = (9, 4)

# TODO: unpack coordinate into two variables named row and col in a single
#       line, then print both
```

## 5.13 Additional practice: Dice statistics — tallying rolls

Nothing new here — just the loop tools from this chapter combined. A
dictionary keyed by every possible sum starts at 0, and a loop full of
dice rolls tallies into it.

```python
import random

counts = {}
for total in range(2, 13):
    counts[total] = 0

# TODO: write a for loop that rolls two six-sided dice 500 times, using
#       random.randint(1, 6) for each die the way the note's dice example
#       does, and tallies each roll's sum into counts
```

## 5.13 Additional practice: Dice statistics — printing the histogram

With `counts` tallied from the cell above, drawing the histogram is a
matter of looping over the dictionary's items and multiplying a string by
each count.

```python
# TODO: loop over counts.items() and print a histogram line for each sum,
#       the way the note's example draws bars with string multiplication
```

Nice work — that covers every loop tool this chapter introduced. Functions are next.

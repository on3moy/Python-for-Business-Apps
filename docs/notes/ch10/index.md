# Chapter 10

Classes — how to stop passing loose variables around and start grouping data and behavior into your own types, the same way Python already did for strings and lists.  

- [10.1 Classes: Introduction](10.1-classes-introduction.md) — what an object is, and why grouping data and functions together makes programs easier to reason about
- [10.2 Classes: Grouping data](10.2-classes-grouping-data.md) — the `class` keyword, `__init__`, `self`, and creating instances
- [10.3 Instance methods](10.3-instance-methods.md) — functions defined inside a class, and the classic mistake of forgetting `self`
- [10.4 Class and instance object types](10.4-class-and-instance-object-types.md) — attributes shared by every instance vs. attributes unique to one
- [10.5 Class example: Putting it together](10.5-class-example-putting-it-together.md) — one class managing a collection of instances of another
- [10.6 Class constructors](10.6-class-constructors.md) — constructor parameters and default values
- [10.7 Class interfaces](10.7-class-interfaces.md) — the methods a user is meant to call, and the underscore convention for the ones they aren't
- [10.8 Class customization](10.8-class-customization.md) — `__str__()` and overloading comparison operators like `<`
- [10.9 More operator overloading: Classes as numeric types](10.9-numeric-operator-overloading.md) — teaching your class to work with `+`, `-`, and friends, safely
- [10.10 Memory allocation and garbage collection](10.10-memory-allocation-and-garbage-collection.md) — what's happening under the hood every time you create an object

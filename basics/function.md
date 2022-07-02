# Advanced Topics in Function

## Default arguments

```python

def printinfo( name, age = 35):
  print(name, "is", age, "years old".)

printinfo("Alice", 30)
printinfo("Alice")

```

## Variable-length arguments

- If you need to process a function for more arguments than you specified while defining the function, use variable-length arguments.

```python

def printinfo( name, *vartuple):
  print(name, ":")
  for i in vartuple: print i

printinfo("Alice", 30)
printinfo("Alice", 40, 50, 60, 70)

```

## Anonymous functions

- declare using `lambda` keyword
- can take any number of arguments, but can only have one expression
- `lambda arguments: expression`

```python

x = lambda a: a + 10
print(x(5))

product = lambda a, b: a * b
print(product(5, 100))

sum = lambda a, b, c: a + b + c
print(sum(10, 20, 30))

```

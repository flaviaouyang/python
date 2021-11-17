# Automate the boring stuff with Python

- Run python in terminal `python filename.py`
- Run python in VSC `shift + 1`

## Chapter One: Python Basics

- Math Operator

  ```python
  ** #exponent
  % #modulus/remainder
  // #integer division/floored quotient
  ```

- Variable naming convention: `snake_case`

- Typecasting: `str(100)`,`int("100")`,`float(100)`

## Chapter Two: Flow Control

- Comparison Operators

```python
== # equal to
!= # not equal to
```

- Boolean Operators

```python
True and True # True
True and False # False
False and True # False
False and False # False
# there is no bool(input()) in Python
```

- if statements

```python
if condition == "True":
  print ("This code block will run.")
 print("If condition is false, the code block above will not run.")

if password == "Flavia is great":
  print("Access Granted")
else:
  print("Access Denied")
  
if sex == "female":
  print("Welcome")
elif sex == "non-binary":
  print("Come on in")
elif sex == "male":
  print("Get the fuck away")
else:
  print("Please await assisstance")
```

- While loop

```python
while counter < 10:
  print ("Hello, there!")
  counter += 1
```

- break statement

```python
while True:
  print("enter your name\n")
  name = input()
  if name == "Flavia":
    break
print ("Thank you")
```

- continue statements

```python
# continue statements are used inside loops
# when reaches a continue statement, the program execution jumps back to the start of the loop and reevaluates the loop's condition

while True:
  code = input("What is the code word?")
  if code != "cactus"
  	continue
  else:
    print("Welcome")
  	break
print("You're in.")
```

- for loop
- `range()`

```python
for i in range(12, 16):
  print(i)
# 12 13 14 15
for i in range(0, 10, 2):
  print(i)
# 0 2 4 6 8
for i in range (5, -1, -1):
  print(i)
# 5 4 3 2 1 0
```

- importing modules: `import`statement composed of `import`, the name of the module, comma, and more modules names (optional)

- Ending a Program Early: `sys.exit()`

  - terminate a program by calling `sys.exit()` 
  - since this function is in `sys`module, you have to import `sys`before your program can use it

  ```python
  import sys
  while True:
    response = input("Enter \'exit\' to exit.")
    if response == "exit":
      sys.exit()
     print("Your response is " + response)
  ```

  ## Chapter Three: Functions

  


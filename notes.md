# Automate the boring stuff with Python

- Run python in terminal `python filename.py`
- Run python in VSC `shift + 1`

***

## Chapter One: Python Basics

- Math Operator

  ```python
  ** #exponent
  % #modulus/remainder
  // #integer division/floored quotient
  ```

- Variable naming convention: `snake_case`

- Typecasting: `str(100)`,`int("100")`,`float(100)`

---

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

---

## Chapter Three: Functions

- A *function* is like a min-program within a program

```python
def hello():
  print("Howdy!")
  print("Hallo!")
  print("Salut!")
```

- The first line is a `def`statement which defines a function's name

- code block that follows `:` is the body of the function
- The code is executed when the function is called, not defined
- The `none`value:
  - represents the absence of a value
  - `None` is the only value of the `NoneType`data type
- `print()`function

```python
print("Hello". end="")
print("World")
# HelloWorld
print("cats", "dogs", "mice", sep="-")
```

- Local and Global Scope
  - Parameters and variables that are assigned in a called function are within that function's *local scope*.
  - Variables that are assigned outside all functions are within in the *global scope*.
- Exception Handling
  - an error or *exception* means that the entire program will crash
  - Errors and can be handled with <strong>try and except</strong> statements
    - code that can potentially have an error is put in a **try** clause
    - Program moves to the start of a **except** clause if an error happens

```python
def division(denominator):
  try:
    return 100/denominator
  except ZeroDivisionError:
      print ("Error: Invalid argument.")
```

---

## Chapter four: Lists

- The *List*  Data Type:
  - *List* is a value that contains multiple values in an ordered sequence
  - `list=['a', 'list', 'looks', 'like', 'this']`
  - Values inside the list is called **items**, and items are separated with **commas**.
- Getting individual values in a list with Indexes
  - ![Screen Shot 2021-11-17 at 12.11.41 AM](/Users/flaviaouyang/Library/Application Support/typora-user-images/Screen Shot 2021-11-17 at 12.11.41 AM.png)
  - Python will give an `IndexError`message if an index exceeding the number of values in your list values is given
  - Index can only be integer values, not floats. Otherwise, a `TypeError`will be thrown.
  - Lists can also contain other list values.
  - Negative Indexes: `-1`refers to the last index in a list, so on and so forth
- Getting Sublists with Slice
  - `list[1:10]`
- Getting a list's length with `len()`
- List Concatenation and List Replication
  - `+`operator can combine two lists to create a new list value
  - `*`operator can replicate the list `x`amount of time
- Romving vlues from lists with `del`statements
  - `del`statement will delete values at an index in a list
  - all the values in the list after the deleted value will be moved up one index
  - `del list[index]`
  - `del list` will delete the entire variable 
    - if you try to use the variable after, you will get a `NameError`error
- Working with Lists
  - to avoid using multiple and repetitive variables, you can use a single variable that contains a list value
- `in` and `not in`operators
  - `'cat' in list` or `'boy' not in list`
- Multiple Assignment Trick:
  - `cat=['black','old]`
  - `color = cat[0]`and `age = cat[1]`
  - or you can write `color, age = cat`
  - if the number of variables and the length of the list is not **exactly the same**, a `ValueError`will be thrown.
- Methods: a *method*  is the same thing as a function, except it is "called on" a value.
  - finding a value in alist with the `index()`method
    - `list.index('item')` >>> `2`
    - if the value isn't in the list, a `ValueError`is thrown
    - when there are duplicates in the list, the first appearance is returned
  - adding values to lists with `append()`and `insert()`methods
    - `append('value')`adds to the end of the list
    - `insert(index, 'value')` insert a value at any index
    - both methods can only be used on list values
  - removing values from lists with `remove()`
    - `list/remove('value')`
    - if there are duplicates, <u>only the first instance</u> of the value will removed
  - sorting the values in list with the `sort()`method
    - `list.sort()` will sort numbers in ascending order and string values in ASCIIbetical order (uppercase before lowercase)
    - `list.sort(reverse=True)`
    - you cannot sort lists with multiple data types
    - `list.sort(key=str.lower)`will sort in a regular alphabetical order
- List-like types: Strings and Tuples
- Mutable and Immutable Data Type:
  - Mutable (it can be modified): list
  - Immutable (it cannot be reassigned/rearranged): string
- Tuple: almost identical to list, except that
  - tuples are enclosed with parentheses `()`
  - tuples are immutable
    - no modifying values
    - no appending
    - No removing
  - if there is only one value in a tuple, you must add a trailing comma to indicate that it is a tuple not a string
  - Typecasting: `tuple(list)`
- References
  - When you assign a list to a variable, you are assigning a list *reference* to the variable. 
  - A reference is a value that points to some bit of data and list reference is a value that points to a list
  - Therefore, if you change the list through one reference, the lists changes

```python
dog = ['doberman', 'golden', 'corgi']
dog_1 = dog
dog_1[1] = 20
print (dog)
print (dog_1)

# ['doberman', 20, 'corgi']
# ['doberman', 20, 'corgi']
```

- The copy Module's `copy()`and `deepcopy()`functions
  - first `import copy`
  - `copy.copy(list)`can be used to make a duplicate copy of a mutable value (list or dictionary) not just a copy of reference
  - if the list needs to be copied contains lists, then use `copy.deepcopy()`

---

## Chapter Five: Dictionaries And Structuring Data

- **Dictionary** data type: a collection of many values
	- unlike lists, indexes can be anything not only integers
	- index for dictionary is called **key**
	- A key with its associated value is **key-value pair**
	- Code below assigns a dictionary to `myCat`variable, the `keys` are `size, color,disposition` and `values`are `'big','gray','loud'`

```python
myCat = {'size':'big', 
         'color': 'gray',
         'disposition':'loud'}
```

- Dictionaries vs. Lists

	- items in dictionaries are unordered
	- dictionaries cannot be sliced like lists
	- access a key that does not exist will result in a `KeyError` message

- `keys(), values(), and items()`Methods

	- `dic_name.key()`
	- they are not lists
	- `dic.item()` returns tuples of key and value
	- use `list()` to transform output to list

- Checking if a `key/value`exist in a Dictionary

	- use `in` or `not in` operator

	```python
	print('big' in cat)
	# output:
	# False
	
	print('size' in cat)
	# output:
	# True
	
	print('big' in cat.values())
	# output:
	# True
	```

- `get()`: takes two arguments

	1. key of the value to retrieve
	2. a fallback value to return if that key does not exist

```python
print("The cat is ", cat.get('size', 'undetermined in terms of size'), ".")
# output:
# The cat is  big .

print("The cat is ", cat.get('breed', 'undetermined in terms of breed'), ".")
# output:
# The cat is  undetermined in terms of breed .
```

- `setdefault()`method:
	- set a value for a certain key if that key does not already have a value
	- first argument passed: the key to check for
	- second argument passed: the value set at that key if key DNE
	- if key does exist, the method returns the key's value
- Pretty Printing
	- `import pprint`
	- `pprint.pprint()`
	- `pprint.pformat()` gives the prettified text as a string value
- Using Data Structures to Model Real-World Things 
	- Tic-Tac-Toe Board
- Nested Dictionaries and Lists

---

## Chapter Six: Manipulating Strings

- String Literals

	- double quotes `foo = "this is a string"`

	- escape characters `foo = 'say hi to Nat\'s mother'`

		1. `\s` single quote
		2. `\"` double quote
		3. `\t` tab
		4. `\n` new line
		5. `\\` backslash

	- raw strings: place `r` before the beginning of quotation mark and make it a raw string

		- **a raw string** ignores all escape characters

	- multiline strings with triple quotes

		```python
		print('''Dear Austyn,
		
		I love you more and more each day.
		
		Sincerely,
		Flavia
		''')
		```

		




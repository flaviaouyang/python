# `eval()` method

- The `eval()` function evaluates the specified expression, if the expression is a legal Python statement, it will be executed.
- In other words, the `eval()` method parses the expression passed to this method and runs python expression (code) within the program.

```python
number = 9

# eval performs the multiplication passed as argument
square_number = eval('number * number')
print(square_number)

# Output: 81
```

## Syntax

```python
eval(expression, globals=None, locals=None)
```

- **expression**: the string parsed and evaluated as a Python expression
- **global**: a dictionary
- **locals**: a mapping object
- returns: the result evaluated from the expression

## Warning

- Consider a situation where you are using a Unix system (macOS, Linux etc) and you have imported the os module. The os module provides a portable way to use operating system functionalities like reading or writing to a file.

- If you allow users to input a value using `eval(input())`, the user may issue commands to change file or even delete all the files using the command: `os.system('rm -rf *')`.

## Methods Restriction

- You may need to restrict the use of these methods and variables for `eval()`. You can do so by passing optional globals and locals parameters (dictionaries) to the `eval()` function.

- Possible scenarios:

  1. both global and local omitted: `expression` is executed in the current scope
  2. omit only locals parameter: it defaults to globals dictionary. Meaning, globals will be used for both global and local variables.
  3. make certain methods available
  4. restricting `builtin`: `eval(expression, {'__builtins__': None})`
  5. Passing both globals and locals dictionary: You can make needed functions and variables available for use by passing the locals dictionary.

```python
from math import *
print(eval('dir()', {'sqrt': sqrt, 'pow': pow}))

# output
['__builtins__', 'pow', 'sqrt']

# Here, the expression can only use the sqrt() and the pow() methods along with __builtins__.

names = {'square_root': sqrt, 'power': pow}
print(eval('dir()', names))

# Using square_root in Expression
print(eval('square_root(9)', names))

a = 169
print(eval('sqrt(a)', {'__builtins__': None}, {'a': a, 'sqrt': sqrt}))
```

- Restricting the use of `eval()` by passing globals and locals dictionaries will make your code secure particularly when you are using input provided by the user to the `eval()` method.

## Example

[Visit code examples](https://github.com/flaviaouyang/python/blob/master/basics/eval-method/eval_method.py)

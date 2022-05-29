# The eval() method parses the expression passed to this method and runs python expression (code) within the program.

number = 9

# eval performs the multiplication passed as argument
square_number = eval('number * number')
print(square_number)

# Output: 81

# syntax
# eval(expression, globals=None, locals=None)

# expression - the string parsed and evaluated as a Python expression
# globals (optional) - a dictionary
# locals (optional)- a mapping object. Dictionary is the standard and commonly used mapping type in Python.

# The eval() method returns the result evaluated from the expression.
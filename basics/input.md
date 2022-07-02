# input

## `raw_input()` V.S. `input()`

- `raw_input()`: reads one line from standard input and returns it as a string (removing the trailing newline)
- `input()`: equivalent to `raw_input` except that it assumes the input is a valid Python expression and returns the evaluated result

```python

str = input("Enter your input: ")
print "Received input is : ", str

Enter your input: [x*5 for x in range(2,10,2)]
Received input is : [10, 20, 30, 40]

```

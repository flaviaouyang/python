output = eval("2 ** 2")
print(output)

# output:
# 4

list = [1, 2, 3]
eval("list.extend(list)")
print(list)
# output:
# [1, 2, 3, 1, 2, 3]

from math import *
a = 169
print(eval('sqrt(a)', {'__builtins__': None}, {'a': a, 'sqrt': sqrt}))
# output:
# 13.0

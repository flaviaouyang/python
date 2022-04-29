import pyperclip

# print('''Someone will remember us
# I say
# Even in another time''')

# foo = "cool"
# print(foo.upper())
# FOO = foo.upper()
# trying = "tRy"
# print(trying.isupper())
# all_upper = "BOOKS"
# print(all_upper.isupper())

# id = "SDG75646"
# print(id.isalpha())
# print(id.isalnum())
# print(id.startswith('S'))
# print(id.endswith('6'))

a = 'apple'
b = 'banana'
c = 'cucumber'
d = 'deck'

print(', '.join([a, b, c, d]))

quote = 'Someone will remember us, I say, Even in another time'

print(quote.split(', '))

print(a.rjust(30, "*"))
print(b.ljust(10, "*"))
print(c.center(20, "="))

pyperclip.copy(d)
print(pyperclip.paste())





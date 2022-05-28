# This method checks if all the characters of a string are alphanumeric (a-z, A-Z and 0-9).
print('abc123'.isalnum())
print('abc123.'.isalnum())
# output:
# True
# False

# This method checks if all the characters of a string are alphabetical (a-z and A-Z).
print('abdc'.isalpha())
print('abcd'.isalpha())
print('abcd123'.isalpha())
# output:
# True
# True
# False

# This method checks if all the characters of a string are digits (0-9).
print('1234'.isdigit())
print('1234abc'.isdigit())
# output:
# True
# False

# This method checks if all the characters of a string are lowercase characters (a-z).
print('abcd'.islower())
print('aBcd'.islower())
# output:
# True
# False

# This method checks if all the characters of a string are uppercase characters (A-Z).
print('ABCD'.isupper())
print('ABCd'.isupper())
# output:
# True
# False

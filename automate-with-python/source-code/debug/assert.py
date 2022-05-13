def get_age(age):
    assert age >= 18
    return age

print(get_age(5))

# Traceback (most recent call last):
#   File "/Users/flaviaouyang/Automate-Python/source-code/debug/assert.py", line 5, in <module>
#     print(get_age(5))
#   File "/Users/flaviaouyang/Automate-Python/source-code/debug/assert.py", line 2, in get_age
#     assert age >= 18
# AssertionError
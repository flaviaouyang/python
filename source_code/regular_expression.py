import re
# def isPhoneNumber(input):
#     if len(input) != 12:
#         return False
#     for i in range(0, 3):
#         if not input[i].isdecimal():
#             return False 
#     if input[3] != '-':
#         return False
#     for i in range(4, 7):
#         if not input[i].isdecimal():
#             return False
#     if input[7] != '-':
#         return False
#     for i in range(8, 12):
#         if not input[i].isdecimal():
#             return False
#     return True

# def findPhoneNumber(input):
#     for i in range(len(input)):
#         chunk = input[i:i+12]
#         if isPhoneNumber(chunk):
#             print("Phone number found: " + str(chunk))
#     print("Done!")

message = "He was split, one part of him never left this mental chamber 415-555-9999 that pictured itself as a sphere full of light 778-123-7789 fading into dark, because there was no way out. But motion in this world depended on rest in the world outside. A man is in bed, wanting to sleep. A rat is behind the wall at his head, wanting to move. The man hears the rat fidget and cannot sleep, the rat hears the man fidget and dares not move. They are both unhappy, one fidgeting and the other waiting, or both happy, the rat moving and the man sleeping."
# findPhoneNumber(message)

phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
num = phoneRegex.search(message)
no = phoneRegex.search("i like you")
print(no)
print(num.group())

quote = '''
the last at last seen of him
himself unseen by him
and of himself"

A rest.

The last Mr. Murphy saw of Mr. Endon was Mr. Murphy unseen by Mr. Endon. This was also the last Murphy saw of Murphy."

A rest. 2020-11-20

The relation between Mr. Murphy and Mr. Endon could not have better summed up than by the former's sorrow at seeing himself in the latter's immunity from seeing anything but himself."

A long rest.

Mr. Murphy is a speck in Mr. Endon's unseen.
'''

restRegex = re.compile(r'\d\d\d\d-\d\d-\d\d')
mo = restRegex.search(quote)
print(mo.group())

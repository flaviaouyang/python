# Project: Phone number and email Address extractor
import pyperclip
import re

phone_number_regex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?
    (\s|-|\.)?
    (\d{3})
    (\s|-|\.)
    (\d{4})
    (\s*(ext|x|ext.)\s*(\d{2,5}))?
    )''', re.VERBOSE)

# Create email regex.
email_regex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+
    @
    [a-zA-Z0-9.-]+
    (\.[a-zA-Z]{2,4})
    )''', re.VERBOSE)

# Find matches in clipboard text.
text = str(pyperclip.paste())

phone_found = phone_number_regex.findall(text)
email_found = email_regex.findall(text)
matches = []

for group in phone_found:
    phone_number = '-'.join([group[1], group[3], group[5]])
    if group[8] != '':
        phone_number += 'x' + group[8]
    matches.append(phone_number)
    
for group in email_found:
    matches.append(group[0])
    
# Copy results to the clipboard.
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard: ')
    print('\n'.join(matches))
else:
    print("No phone numbers or emailes found.")
    


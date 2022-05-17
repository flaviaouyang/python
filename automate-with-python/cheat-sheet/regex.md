# Regular Expression Cheat Sheet

- `?` matches zero or one of the preceding group
- `*` matches zero or more of the preceding group
- `+` matches one or more of the preceding group
- `{n}` matches *n* of the preceding group
- `{n,}` matches *n* or more of the preceding group
- `{,m}` matches 0 to *m* of the preceding group
- `{n,m}` matches at least *n* and at most *m* of the preceding group
- `{n,m}?` or `*?` or `+?` performs a nongryeedy match of the preceding group
- `^spam` means the string must begin with *spam*
- `spam$` means the string must end with *spam*
- `.` matches any character with the exception of newline
- `\d` matches a digit
- `\w` matches a word
- `\s` matches a space
- `\D` matches anything except a digit
- `\W` matches anything except a word
- `\S` matches anything except a space
- `[abc]` matches any character between the brackets
- `[^abc]` matches any character that isn't between the brackets


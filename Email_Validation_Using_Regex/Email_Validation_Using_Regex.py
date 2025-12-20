import re


email = "test@gmail.com"
pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

if re.match(pattern, email):
    print("Valid Email")
else:
    print("Invalid Email")


# Regex Patterns Explanation

# \d  -> Matches any digit (0–9)
# \D  -> Matches any non-digit character
# \w  -> Matches letters, digits, and underscore (_)
# \W  -> Matches any character except letters, digits, and underscore
# .   -> Matches any single character except newline
# ^   -> Matches the start of a string
# $   -> Matches the end of a string
# *   -> Matches 0 or more occurrences
# +   -> Matches 1 or more occurrences
# ?   -> Matches 0 or 1 occurrence
# pylint: disable=missing-module-docstring
import re

print("Hello")
in_String = ['(603) 555-1212', '(603) ILL-EGAL','(603) 867-5309']


# regex of matching the entire string (re.match) and part of the string (re.search)
for test_string in in_String:
    if re.match(r'^.\d{3}..\d{3}-\d{4}$', test_string) and re.search(r'\) (?!555-)', test_string):
        print(test_string, 'is a valid US local phone number')
    else:
        print(test_string, 'is not valid and has been rejected')

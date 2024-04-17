#This is a single - line comment
print("Escape Sequence")

'''
This is a multi line comment
This is a multi line comment
This is a multi line comment
This is a multi line comment
This is a multi line comment
'''
"""
Escape Sequence Characters
To insert characters that cannot be directly used in a string, we use an escape sequence character.
An escape sequence character is a backslash \ followed by the character you want to insert.
An example of a character that cannot be directly used in a string is a double quote inside a string that is surrounded by double quotes:
"""

# print("This doesnt "execute")
print("This will \"execute")
print("This will \"execute\"")

print("Hey", 9, 7, 5, sep="~", end="009\n")
print("Hello")

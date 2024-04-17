# Strings in Python

# In python, anything that you enclose between single or double quotation marks is considered a string. 
# A string is essentially a sequence or array of textual data. Strings are used when working with Unicode characters.

name = "Aman"
print("Hello, "+ name)
print('He said, "I want to eat an apple".')

# Multiline Strings
# If our string has multiple lines, we can create them like this:
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# In Python, string is like an array of characters. We can access parts of string by using its index which starts from 0.
print(name[0], name[1])


# Looping through the string
# We can loop through strings using a for loop like this:
for character in name:
    print(character)
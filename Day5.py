#Typecasting
'''
The conversion of one data type into the other data type is known as type casting in python or type conversion in python.
Python supports a wide variety of functions or methods like: int(), float(), str(), ord(), hex(), oct(), tuple(), set(), list(), dict(), etc. for the type casting in python.
'''
# Two Types of Typecasting:
# Explicit Conversion (Explicit type casting in python)
# Implicit Conversion (Implicit type casting in python).

a  = "30"
b = "70"
print(a + b)
print("Typecasting: ", int(a) + int(b))

# Implicit type casting:
"""
Data types in Python do not have the same level i.e. ordering of data types is not the same in Python. Some of the data types have higher-order, and some have lower order. While performing any operations on variables with different data types in Python, one of the variable's data types will be changed to the higher data type. 
According to the level, one data type is converted into other by the Python interpreter itself (automatically). This is called, implicit typecasting in python.
Python converts a smaller data type to a higher data type to prevent data loss.
"""

# Python automatically converts
# a to int
a = 7
print(type(a))

# Python automatically converts b to float
b = 3.0
print(type(b))
 
# Python automatically converts c to float as it is a float addition
c = a + b
print(c)
print(type(c))

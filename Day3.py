# Variables and Data Types
a = 90
d = None
print("The type of a is", type(a))
print("The type of d is", type(d))


c = 1.1
print("The type of c is", type(c))
# v = 7 + 4i
z = complex(8,9)
print("z is", z)
print("The type of z is", type(z))


# Sequenced data: list, tuple
# list: A list is an ordered collection of data with elements separated by a comma and enclosed within square brackets. Lists are mutable and can be modified after creation.
list1 = [8, 2.3, [-4,5], ["apple","banana"]]
print(list1)

# Tuple: A tuple is an ordered collection of data with elements separated by a comma and enclosed within parentheses. Tuples are immutable and can not be modified after creation.
tuple1 = (("parrot", "sparrow"), ("Lion", "Tiger"))
print(tuple1)

# Mapped data: dict
# dict: A dictionary is an unordered collection of data containing a key:value pair. The key:value pairs are enclosed within curly brackets.
dict1 = {"name":"Sakshi", "age":20, "canVote":True}
print(dict1)

# In python everthing is an object
# ForLoops
# for loops can iterate over a sequence of iterable objects in python. Iterating over a sequence is nothing but iterating over strings, lists, tuples, sets and dictionaries.
# Example: iterating over a string:
# name = "Aman Sharma"
# for i in name:
#     print(i, end=(" "))


# Example: iterating over a list:
colors = ["Red", "Green", "Blue", "Yellow"]
for x in colors:
    print(x)
# Similarly, we can use loops for lists, sets and dictionaries.

# range():
# What if we do not want to iterate over a sequence? What if we want to use for loop for a specific number of times? Here, we can use the range() function.
'''Syntax
range(start, stop, step)
start: The starting value of the sequence (inclusive). This is where the sequence begins.
stop: The ending value of the sequence (exclusive). The sequence will stop before reaching this value.
step: The difference between each consecutive number in the sequence. This can be positive or negative.
'''


for k in range(5):
    print(k)

for k in range(4,9): #4 to 8
    print(k)

# range from 0 up to (but not including) 10, with a step of 2
for i in range(0, 10, 2):
    print(i, end=(" "))  # Output: 0, 2, 4, 6, 8












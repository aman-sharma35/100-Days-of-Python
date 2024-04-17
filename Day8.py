# String Slicing and Operations on Strings

name = "AmanisRevisingPython"
print(name[0:4]) #including 0  but not 4
print(len(name))

pie = "ApplePie"
print(pie[:5])
print(pie[6])	#returns character at specified index
print(pie[:-3])
print(pie[:len(pie) -3])
# print(pie[:-3]) and print(pie[:len(pie) -3]) means the same as python automatically puts len function

print(pie[-1:len(pie) -3]) #print nothing
#  pie[-1] this means pie[len(pie) -1] which is 8-1 = 7, and pie[len(pie) -3] is 8 -3 = 5 so, 7:5 makes no sense
print(pie[-3:len(pie) -1])
# pie[len(pie) - 3] is 8 - 3 = 5, and pie[len(pie) -1] is 8 - 1 = 7 so, 5:7 so it will print Pi which is index 5 ans 6

"""
Loop through a String:
Strings are arrays and arrays are iterable. Thus we can loop through strings.
"""
alphabets = "ABCDE"
for i in alphabets:
    print(i)

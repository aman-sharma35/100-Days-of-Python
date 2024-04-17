# Match Case Statements
# For developers coming from languages like C/C++ or Java know that there was a conditional statement known as Switch Case. This Match-Case is the Switch Case of Python which was introduced in Python 3.10. Here we have to first pass a parameter then try to check with which case the parameter is getting satisfied. If we find a match we will do something and if there is no match at all we will do something else.

'''The match case consists of three main entities :
The match keyword
One or more case clauses
Expression for each case'''

x = 4
# x is the variable to match
match x:
    # if x is 0
    case 0:
        print("x is zero")
    # case with if-condition
    case 4 if x % 2 == 0:
        print("x % 2 == 0 and case is 4")
    # Empty case with if-condition
    case _ if x < 10:
        print("x is < 10")
    # default case(will only be matched if the above cases were not matched)
    # so it is basically just an else:
    case _:
        print(x)











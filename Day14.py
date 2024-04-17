# While Loop
# while loops execute statements while the condition is True. As soon as the condition becomes False, the interpreter comes out of the while loop.

count = 5
while (count > 0):
  print(count)
  count = count - 1

# We can even use the else statement with the while loop. Essentially what the else statement does is that as soon as the while loop condition becomes False, the interpreter comes out of the while loop and the else statement is executed.

x = 5
while (x > 0):
    print(x)
    x = x - 1
else:
    print('counter is 0')


# How Can You Emulate Do-While Loops in Python?
# The most common technique to emulate a do-while loop in Python is to use an infinite while loop with a break statement wrapped in an if statement that checks a given condition and breaks the iteration if that condition becomes true:
# while True:
#     # Do some processing...
#     # Update the condition...
#     if condition:
#         break
# Emulating a do-while loop in Python
while True:
    # Code block to be executed
    print("Hello, this will execute at least once.")
    
    # Condition check to continue or break the loop
    user_input = input("Do you want to repeat? (yes/no): ").strip().lower()
    
    if user_input != 'yes':
        break


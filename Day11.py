import time
# timestamp = time.strftime('%H:%M:%S')
# print(timestamp)
# timestamp = time.strftime('%H')
# print(timestamp)
# timestamp = time.strftime('%M')
# print(timestamp)
# timestamp = time.strftime('%S')
# print(timestamp)
# https://docs.python.org/3/library/time.html#time.strftime

name = input("Enter your name: ")
recenttime = time.strftime('%H:%M:%S')
RecentTime = int(time.strftime("%H"))

if(4 <= RecentTime < 12):
    print("Good Morning!! ",name,"It,s ",recenttime)
elif(12 <= RecentTime < 17):
    print("Good Afternoon!! ",name,"It,s ",recenttime)
else:
    print("Good Night!! ",name,"It,s ",recenttime)


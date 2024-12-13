# Write a python program to check given string is even length or not.

# Input:
# enter your name: Sushil

# Output:
# Even

# Program

name = input("enter your name: ")
length = len(name)

if(length % 2 == 0):
    print("Even")
else:
    print("Not even")

# Q. Write a python program to display reverse string.

# Input:
# enter your name: Sushil

# Output:
# Original string
# Sushil
# Reverse string
# lihsuS

# Program 
name = input("enter your name: ")
size = len(name)-1
reverse = ""


print("Original string")
print(name)
for i in range(size, -1, -1):
    reverse += name[i]

print("Reverse string")
print(reverse)
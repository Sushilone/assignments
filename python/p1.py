# Q. Display design pattern in python
"""
*
**
***
****
*****

"""

# Input:
# enter a number: 5


# Output:
# *
# **
# ***
# ****
# *****

# Program code
n = int(input("enter a number: "))

for i in range(n):
    for j in range(i+1):
        print("*", end="")
    print()
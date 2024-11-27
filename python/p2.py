# Q. Display design pattern in python.
"""
1
22
333
4444
55555

"""
# Input:
# enter a number: 5

# Output:
# 1
# 22
# 333
# 4444
# 55555

# Program code
n = int(input("enter a number: "))
for i in range(n):
    for j in range(i+1):
        print(i+1,end="")
    print()
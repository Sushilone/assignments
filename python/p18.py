# Python program to display the given integer in a reverse manner.

# Input:
# enter an integer number: 123

# Output: 
# Integer in reverse manner: 321


num = int(input("enter an integer number: "))
rev = 0

while(num > 0):
    rem = num % 10
    rev = (rev * 10) + rem
    num = num // 10

print("Integer in reverse manner: ",rev)
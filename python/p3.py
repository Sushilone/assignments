# Q. Write a program to check a given number is prime number or not.


# Input: 
# enter a number: 5


# Output:
# 5 is a prime number.

# Program code
n = int(input("enter a number: "))

flg=0
for i in range(2,n):
    if(n%i==0):
        flg=1

if(flg):
    print(n ,"is not a prime number.")
else:
    print(n ,"is a prime number.")
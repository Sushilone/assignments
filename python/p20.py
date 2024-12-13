# Python program to find the factorial of a number using recursion.

# Input:
# enter a number: 3

# Output:
# factorial of 3 is: 6

def factorial(n):
    if(n==1):
        return 1
    return n * factorial(n-1)

n = int(input("enter a number: "))

print("factorial of ", n, "is: ", factorial(n))


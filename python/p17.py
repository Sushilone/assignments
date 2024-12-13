# Python program to find the average of 10 numbers using while loop.

# Input:
# enter 10 numbers: 
# enter number: 10
# enter number: 9
# enter number: 8
# enter number: 7
# enter number: 6
# enter number: 5
# enter number: 4
# enter number: 3
# enter number: 2
# enter number: 1

# Output:
# Average is:  5.5


numbers = 0
print("enter 10 numbers: ")

i = 0
while( i < 10):
    n = int(input("enter number: "))
    numbers += n
    i += 1

avg = numbers/10
print("Average is: ",avg)
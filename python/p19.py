# Python program to generate the prime numbers from 1 to N

# Input:
# enter n: 20

# Output:
# Prime numbers 1 to  20
# [1, 2, 3, 5, 7, 11, 13, 17, 19]

numbers, primes = [], []

n = int(input("enter n: "))

for i in range(1, n+1):
    numbers.append(i)


for i in range(1, n):
    if(numbers[i]==0):
        continue
    for j in range(i+1, n):
        if(numbers[j] % numbers[i] == 0):
            numbers[j] = 0


for i in numbers:
    if(i != 0):
        primes.append(i)

print("Prime numbers 1 to ",n)
print(primes)
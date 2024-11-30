# Q.Write a python code to recursively find the power of a number.

# Input:
# enter number: 2
# enter power: 4

# Output:
# 2 raise to power 4 is 16

def pwr(n,p):
    if(p==1):
        return n
    return n*pwr(n,p-1)

n = int(input("enter number: "))
p = int(input("enter power: "))

res = pwr(n,p)
print(f"{n} raise to power {p} is {res}")




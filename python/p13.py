# Write a python program to find the sum of all items in a dictionary.

# Output:
# {'apples': 3, 'mangoes': 5, 'bananas': 7}
# Sum of all fruits
# 15

fruits = {
    "apples": 3,
    "mangoes": 5,
    "bananas": 7
}

print(fruits)
sum = 0
for i in fruits:
    sum += fruits[i]  # Calculating sum of fruits

print("Sum of all fruits")
print(sum)
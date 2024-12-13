# Q. Python program to interchange first and last elements in a list.


# Output:
# Before change
# [1, 4, 3, 2, 5, 7]
# After change
# [7, 4, 3, 2, 5, 1]

# Program code

lst = [1, 4, 3, 2, 5, 7]

print("Before change")
print(lst)

temp = lst[0]
lst[0] = lst[5]
lst[5] = temp

print("After change")
print(lst)
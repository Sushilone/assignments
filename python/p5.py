# Q. Create "list" and use insert(), append() method on created list.


# Output:
# [0, 1, 2, 3, 4]

# After insert(2,9)
# [0, 1, 9, 2, 3, 4]

# After append(10)
# [0, 1, 9, 2, 3, 4, 10]


# Program code
lst = [0, 1, 2, 3, 4]
print(lst)
print()

print("After insert(2,9)")
lst.insert(2,9)
print(lst)
print()

print("After append(10)")
lst.append(10)
print(lst)

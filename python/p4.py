# Q. Create "list" data sequence by list() constructor and display it's item from last.


# Output:
# 5
# 4
# 3
# 2
# 1

# Program code
lst = list((1, 2, 3, 4, 5))
size = len(lst)-1

for i in range(size, -1, -1):
    print(lst[i])
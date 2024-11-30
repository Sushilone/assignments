# Q. How to create tuple with one item and change tuple old item value with new itme value.


# Output:
# Before change
# (2,)
# After change
# (4,)


tpl = (2,)

print("Before change")
print(tpl)

lst = list(tpl)
lst[0] = 4
tpl = tuple(lst)

print("After change")
print(tpl)
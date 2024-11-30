# Q. Create tuple x = ("MCA", "MSCIT", "PGDCA") and add item "BCA" in this tuple

# Output:
# Before adding 
# ('MCA', 'MSCIT', 'PGDCA')
# After adding 
# ('MCA', 'MSCIT', 'PGDCA', 'BCA')

# Program code 

tpl = ("MCA", "MSCIT", "PGDCA")
lst = list(tpl)
lst.append("BCA")

print("Before adding ")
print(tpl)
tpl = tuple(lst)
print("After adding ")
print(tpl)
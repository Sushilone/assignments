# .Q Create dictionary car = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }
#    add new item "color": "Red" and display its keys and item.


# Output:
# Before adding
# {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
# After adding
# {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'Red'}

# Program code 
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print("Before adding")
print(car)
car["color"]="Red"
print("After adding")
print(car)
# PRINTING LIST ELEMENTS USING FOR LOOP 


grocery_list = [
    "Shampoo",
    "Soap",
    'Alcohol',
    "Meat",
    "Tomato Sauce",
    "Coffee",
    "Milk",
    "Diaper"
]

print('\n\nMy Grocery List\n')
for i in range(0, len(grocery_list)):
    print(f'Item #{i + 1} - ', grocery_list[i])
print('\n\n')

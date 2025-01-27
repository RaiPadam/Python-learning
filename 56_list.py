shopping_cart = []

# You need to purchase 5 items.
for i in range(5):
    item = input("Enter item: ")
    shopping_cart.append(item) 

# At the end to display all items.

print("All Items are: ")
for i in range(5):
    print(f"{shopping_cart[i]}")
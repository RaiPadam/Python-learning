# Original tuple
names = ("Binaya Shrestha", "Dilip Karki", "Diwash")

# Create a new tuple with the modified element
names = (names[0], "Diwash Karki", names[2])

# Print the updated tuple
print(names)

# Check if "Diwash" is in the tuple
if "Diwash" in names:
    print("Diwash is in the tuple")
else:
    print("Diwash is not in the tuple")
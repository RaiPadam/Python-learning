# Original tuple
names = ("Binaya Shrestha", "Dilip Karki", "Diwash")

# Create a new tuple with "Kishor Saud" inserted at index 1
names = names[:1] + ("Kishor Saud",) + names[1:]

# Print the updated tuple
print(names)

# Check if "Diwash" is in the tuple
if "Diwash" in names:
    print("Diwash is in the tuple")
else:
    print("Diwash is not in the tuple")
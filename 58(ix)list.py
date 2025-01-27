# Original tuple
names = ("Binaya Shrestha", "Dilip Karki", "Diwash")

# Create a new tuple with "Kishor Saud" inserted at index 1
names = names[:1] + ("Kishor Saud",) + names[1:]

# Iterate and print each name
for name in names:
    print(f"Name: {name}")
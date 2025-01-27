names = ("Binaya Shrestha", "Dilip Karki", "Diwash")

# Convert tuple to list to allow modifications
names_list = list(names)
names_list.insert(1, "Kishor Saud")
names = tuple(names_list)  # Convert it back to a tuple

print(names)

mylist = ['apple', 'banana', 'cherry']
mylist[0] = 'kiwi'
print(mylist[1])

if "Diwash" in names:
    print("Diwash is in the names tuple.")

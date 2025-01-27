# Original tuple of names
names = ("Som Prakash Chaudhary", "Nishan Poudel", "Shankar Khadka", "Raj Poudel", "Diwash Sharma Acharya")

# List comprehension to filter names starting with "D" (case-insensitive)
namesstartwithd = [x for x in names if x.lower().startswith("d")]

# Example of using startswith on a single string
name = "Diwash Sharma Acharya"
print(name.startswith("D"))  # This will print True

# Print the filtered list
print(namesstartwithd)
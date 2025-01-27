import random

# Read names from the file
with open("names.txt", "r") as f:
    names = f.readlines()

# Remove newline characters from each name
names = [name.strip("\n") for name in names]

# Function to greet a specific name
def greet(name):
    print(f"Good morning, {name}!")

# Example: Greet a random name from the list
random_name = random.choice(names)
greet(random_name)
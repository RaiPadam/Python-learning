import random                             # Create 3 Lucky Winner from names.txt file using random
print("Lucky Winner Name")
f = open("names.txt", "r")

names = f.readlines()

winner1 = random.choice(names)
winner2 = random.choice(names)
winner3 = random.choice(names)

print(f"The Winner is: {winner1}")
print(f"The Winner is: {winner2}")
print(f"The Winner is: {winner3}")
import random                         # Say Good morning to all friends from names.txt
f = open("names.txt", "r")

names = f.readlines()
for i in range(len(names)):
    names[i] = names[i].strip("\n")
def greet(n):
    print(f"Good morning {n}")

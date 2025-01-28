name = input("Enter your name: ")
file = open("names.txt", "a")
file.write(f"{name}\n")
file.close()
print("File Write Success")

# Compare this snippet from Python%20learning/74read.py:
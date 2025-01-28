
address = input("Enter your address: ")
file = open("address.txt", "w")
file.write(address)
file.close()
print("File Write Success")
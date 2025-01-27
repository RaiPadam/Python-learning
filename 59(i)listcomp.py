names = ("Som Prakash Chaudhary", "Nishan Poudel", "Shankar Khadka", "Raj Poudel")

start_with = input("Enter the starting letter of the name: ")
names_start_with = [x for x in names if x.startswith(start_with)]

print(names_start_with)
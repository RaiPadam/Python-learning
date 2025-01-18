#count the length of total words

text = input("Enter your name: ")

length = len(text)

print(f"Length of your name:{length}")

### create a program that calculate length and total words in a string

list = text.split(" ")

total = len(list)

print(f"Total words :{total}")
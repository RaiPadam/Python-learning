word = input("Enter word: ")

first_char = word[0].lower()
if first_char == "a" or first_char == "e" or first_char == "i" or first_char == "o" or first_char == "u":
    print("Vowel")
else:
    print("Consonant")
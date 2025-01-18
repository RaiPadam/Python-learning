english = float(input("Enter mark in english out of 50: "))
nepali = float(input("Enter mark in nepali out of 50: "))
science = float(input("Enter mark in science out of 50: "))
math = float(input("Enter mark in math out of 50: "))
social = float(input("Enter mark in social out of 50: "))

total = english + nepali + science + math + social
percentage = (total / 250)*100
print(f"Total marks obtained in major five subjects is {total}")
print(f"Percentage is {percentage}")

english = 48
nepali = 48
math = 48
science = 46
social = 47

total = english + nepali + math + science + social
print(total)

percentage = (total / 250) * 100
print("percentage is {percentage}")
fruits = ['Apple', 'Orange', 'Mango']
# make all list upper case
fruits = [r.upper() for r in fruits]
# Make all list upper case
fruit_name = input("Enter a fruit name: ")

if fruit_name.upper() in fruits:
    print(f"{fruit_name} is available")
else:
    print(f"{fruit_name} is not available")
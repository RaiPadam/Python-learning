n1 = 10
n2 = 101
n3 = 105

if n1> n2 and n1> n3:
    print(f"{n1} is greater than {n2} and {n3}")
elif n2 > n1 and n2 > n3:
    print(f"{n2} is greater than {n1} and {n3}")
elif n3 > n1 and n3 > n2:
    print(f"{n3} is greater than {n1} and {n2}")
else:
    print("Something went wrong")

# and
# True and True is True
# True and False is False
# False and True is False
# False and False is False

# or 
# True or True is True
# True or False is True
# False or True is False
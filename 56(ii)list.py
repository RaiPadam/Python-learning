def check_name_in_list(name, name_list):
    if name in name_list:
        print(f"{name} is in the list")
    else:
        print(f"{name} is not in the list")

names = ["Binaya Shrestha", "Dilip Karki", "Diwash"]
check_name_in_list("Diwash", names)
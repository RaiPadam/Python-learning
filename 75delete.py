import os

try:
    os.remove("name.txt")
    print("File deleted successfully")
except FileNotFoundError:
    print("File not found")
except Exception as e:
    print(f"An error occurred: {e}")
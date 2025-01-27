import tkinter as tk

root = tk.Tk()
root.title("Padam Bahadur Rai Bill Split Software")

root.mainloop()

# Simple interest calculate.

principle = int(input("Enter the principl: "))
rate = int(input("Enter the rate: "))
time = int(input("Enter the time: "))

simple_interest = principle * rate * time / 100
print(f"Simple interest is {simple_interest}")
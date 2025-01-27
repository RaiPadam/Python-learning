import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        total_amount = float(textbox1.get())
        total_person = float(textbox2.get())
        
        if total_person <= 0:
            messagebox.showerror("Error", "Number of people must be greater than 0.")
            return
        
        amount_per_person = total_amount / total_person
        result_label.config(text=f"Each person needs to pay Rs. {amount_per_person:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers in both fields.")

# Create the main window
root = tk.Tk()
root.title("Bishworaj Bill Split Software")
root.geometry("500x500")

# Label and Entry for Total Amount
label1 = tk.Label(root, text="Enter Total Amount: ")
label1.pack(pady=10)

textbox1 = tk.Entry(root)
textbox1.pack(pady=5)

# Label and Entry for Total People
label2 = tk.Label(root, text="Enter Total People: ")
label2.pack(pady=10)

textbox2 = tk.Entry(root)
textbox2.pack(pady=5)

# Calculate Button
button1 = tk.Button(root, text="Calculate", command=calculate)
button1.pack(pady=20)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=20)

# Start the main loop
root.mainloop()
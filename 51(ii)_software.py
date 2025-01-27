import tkinter as tk
from tkinter import messagebox

def Calculate():
    try:
        Principal = int(textbox1.get())  # Corrected variable name
        Time = int(textbox2.get())
        Rate = int(textbox3.get())

        # Calculate Simple Interest
        Simple_interest = (Principal * Time * Rate) / 100
        result_label.config(text=f"Simple Interest (SI): Rs. {Simple_interest:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers in all fields.")

# Create the main window
root = tk.Tk()
root.title("Software of Simple Interest (SI)")
root.geometry("600x600")

# Label and Entry for Principal
label1 = tk.Label(root, text="Enter Principal (P): ")
label1.pack(pady=10)

textbox1 = tk.Entry(root)
textbox1.pack(pady=5)

# Label and Entry for Time
label2 = tk.Label(root, text="Enter Time (T): ")  # Corrected class name
label2.pack(pady=10)

textbox2 = tk.Entry(root)
textbox2.pack(pady=5)

# Label and Entry for Rate
label3 = tk.Label(root, text="Enter Rate (R): ")  # Corrected class name
label3.pack(pady=10)

textbox3 = tk.Entry(root)
textbox3.pack(pady=5)

# Calculate Button
button1 = tk.Button(root, text="Calculate", command=Calculate)  # Corrected function name
button1.pack(pady=20)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=20)

# Start the main loop
root.mainloop()
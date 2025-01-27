import tkinter as tk

def Calculate():
    Principal = int(textbox1.get())
    Time = int(textbox2.get())
    Rate = int(textbox3.get())

    Simple_interest = (Principal * Time * Rate / 100)
    result_label.config(text=f"Simple interest (SI) Rs. {Simple_interest:.2f}")

root = tk.Tk()
root.title("Software of Simple Interest (SI)")
root.geometry("600x600")

label1 = tk.Label(root, text="Enter Principal (P): ")
label1.pack()

textbox1 = tk.Entry(root)
textbox1.pack(pady=5)

label2 = tk.Label(root, text="Enter Time (T): ")
label2.pack(pady=5)

textbox2 = tk.Entry(root)
textbox2.pack(pady=5)

label3 = tk.Label(root, text="Enter Rate (R): ")
label3.pack(pady=5)

textbox3 = tk.Entry(root)
textbox3.pack(pady=5)

button1 = tk.Button(root, text="Calculate", command=Calculate)
button1.pack(pady=5)

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
import tkinter as tk
from tkinter import messagebox
import qrcode
from PIL import Image, ImageTk

def generate_qr():
    # Get the input values
    ssid = ssid_entry.get()
    password = password_entry.get()
    phone = phone_entry.get()
    address = address_entry.get()

    if not ssid or not password or not phone or not address:
        messagebox.showerror("Input Error", "Please fill out all fields")
        return

    # Generate Wi-Fi QR Code
    wifi_data = f"WIFI:T:WPA;S:{ssid};P:{password};;"
    wifi_qr = qrcode.make(wifi_data)

    # Generate vCard for phone and address
    vcard_data = f"BEGIN:VCARD\nVERSION:3.0\nFN:{phone}\nADR:{address}\nTEL:{phone}\nEND:VCARD"
    vcard_qr = qrcode.make(vcard_data)

    # Combine QR codes into one image (optional, you can display them separately)
    wifi_qr = wifi_qr.convert('RGB')
    vcard_qr = vcard_qr.convert('RGB')
    
    # Save QR code images
    wifi_qr.save("wifi_qr.png")
    vcard_qr.save("vcard_qr.png")

    # Display the QR code image in the GUI
    display_qr(wifi_qr)

def display_qr(qr_image):
    # Convert the QR image to something that can be displayed in tkinter
    qr_image.thumbnail((250, 250))  # Resize to fit the GUI window
    qr_photo = ImageTk.PhotoImage(qr_image)

    qr_label.config(image=qr_photo)
    qr_label.image = qr_photo  # Keep a reference to the image

# Create the main window
root = tk.Tk()
root.title("QR Code Generator")

# Create and place the labels and input fields
tk.Label(root, text="Wi-Fi SSID:").pack(pady=5)
ssid_entry = tk.Entry(root, width=40)
ssid_entry.pack(pady=5)

tk.Label(root, text="Wi-Fi Password:").pack(pady=5)
password_entry = tk.Entry(root, width=40, show="*")
password_entry.pack(pady=5)

tk.Label(root, text="Phone Number:").pack(pady=5)
phone_entry = tk.Entry(root, width=40)
phone_entry.pack(pady=5)

tk.Label(root, text="Address:").pack(pady=5)
address_entry = tk.Entry(root, width=40)
address_entry.pack(pady=5)

# Create a button to generate the QR code
generate_button = tk.Button(root, text="Generate QR Code", command=generate_qr)
generate_button.pack(pady=10)

# Label to display QR code
qr_label = tk.Label(root)
qr_label.pack(pady=10)

# Start the GUI loop
root.mainloop()

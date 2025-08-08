import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os

def load_image():
    global img, img_path
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        img_path = file_path
        img = Image.open(file_path)
        img_resized = img.resize((250, 250))
        img_tk = ImageTk.PhotoImage(img_resized)
        canvas.create_image(0, 0, anchor=tk.NW, image=img_tk)
        canvas.image = img_tk  # Prevent garbage collection
        status_label.config(text="Image Loaded")

def encrypt_image():
    if not img:
        messagebox.showwarning("No Image", "Please load an image first.")
        return

    encrypted_img = img.copy()
    pixels = encrypted_img.load()

    width, height = encrypted_img.size
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y][:3]
            pixels[x, y] = ((r + 50) % 256, (g + 50) % 256, (b + 50) % 256)

    save_path = os.path.splitext(img_path)[0] + "_encrypted.png"
    encrypted_img.save(save_path)
    messagebox.showinfo("Success", f"Encrypted image saved as:\n{save_path}")

def decrypt_image():
    if not img:
        messagebox.showwarning("No Image", "Please load an image first.")
        return

    decrypted_img = img.copy()
    pixels = decrypted_img.load()

    width, height = decrypted_img.size
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y][:3]
            pixels[x, y] = ((r - 50) % 256, (g - 50) % 256, (b - 50) % 256)

    save_path = os.path.splitext(img_path)[0] + "_decrypted.png"
    decrypted_img.save(save_path)
    messagebox.showinfo("Success", f"Decrypted image saved as:\n{save_path}")

# GUI Setup
root = tk.Tk()
root.title("Image Encryption Tool")
root.geometry("600x400")
root.configure(bg="#1f1f2e")

tk.Label(root, text="SkillCraft Image Encryption Tool", font=("Helvetica", 16, "bold"), fg="white", bg="#1f1f2e").pack(pady=10)

canvas = tk.Canvas(root, width=250, height=250, bg="white")
canvas.pack()

btn_frame = tk.Frame(root, bg="#1f1f2e")
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Load Image", command=load_image, width=15, bg="#3c3c4d", fg="white").grid(row=0, column=0, padx=10)
tk.Button(btn_frame, text="Encrypt", command=encrypt_image, width=15, bg="#3c3c4d", fg="white").grid(row=0, column=1, padx=10)
tk.Button(btn_frame, text="Decrypt", command=decrypt_image, width=15, bg="#3c3c4d", fg="white").grid(row=0, column=2, padx=10)

status_label = tk.Label(root, text="", bg="#1f1f2e", fg="lightgreen")
status_label.pack()

img = None
img_path = ""

root.mainloop()

import tkinter as tk
from tkinter import messagebox

# Caesar Cipher logic
def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

# GUI Functions
def encrypt_text():
    text = input_text.get("1.0", tk.END).strip()
    try:
        shift = int(shift_entry.get())
        encrypted = caesar_encrypt(text, shift)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, encrypted)
    except ValueError:
        messagebox.showerror("Invalid Input", "Shift must be an integer.")

def decrypt_text():
    text = input_text.get("1.0", tk.END).strip()
    try:
        shift = int(shift_entry.get())
        decrypted = caesar_decrypt(text, shift)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, decrypted)
    except ValueError:
        messagebox.showerror("Invalid Input", "Shift must be an integer.")

# GUI Setup
root = tk.Tk()
root.title("Caesar Cipher - Encrypt & Decrypt")
root.geometry("500x400")
root.config(bg="#1f1f2e")

title_label = tk.Label(root, text="Caesar Cipher Tool", font=("Helvetica", 16, "bold"), bg="#1f1f2e", fg="white")
title_label.pack(pady=10)

input_label = tk.Label(root, text="Enter your message:", bg="#1f1f2e", fg="white")
input_label.pack()
input_text = tk.Text(root, height=5, width=50)
input_text.pack(pady=5)

shift_label = tk.Label(root, text="Shift value:", bg="#1f1f2e", fg="white")
shift_label.pack()
shift_entry = tk.Entry(root)
shift_entry.pack(pady=5)

button_frame = tk.Frame(root, bg="#1f1f2e")
button_frame.pack(pady=10)

encrypt_btn = tk.Button(button_frame, text="Encrypt", width=15, command=encrypt_text, bg="#3c3c4d", fg="white")
encrypt_btn.grid(row=0, column=0, padx=10)

decrypt_btn = tk.Button(button_frame, text="Decrypt", width=15, command=decrypt_text, bg="#3c3c4d", fg="white")
decrypt_btn.grid(row=0, column=1, padx=10)

output_label = tk.Label(root, text="Output:", bg="#1f1f2e", fg="white")
output_label.pack()
output_text = tk.Text(root, height=5, width=50)
output_text.pack(pady=5)

root.mainloop()

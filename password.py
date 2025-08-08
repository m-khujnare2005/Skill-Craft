import tkinter as tk
from tkinter import messagebox
import re

def check_password_strength():
    password = entry.get()
    score = 0
    remarks = ""

    # Criteria checks
    if len(password) >= 8:
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[0-9]", password):
        score += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    # Feedback
    if score == 0:
        remarks = "Very Weak: Add characters."
    elif score == 1 or score == 2:
        remarks = "Weak: Add more variety (e.g., numbers, symbols)."
    elif score == 3:
        remarks = "Moderate: Try to include special characters."
    elif score == 4:
        remarks = "Strong Password!"
    elif score == 5:
        remarks = "Very Strong Password!"

    result_label.config(text=f"Strength: {remarks}")

# GUI setup
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x300")
root.configure(bg="#2b2b2b")

tk.Label(root, text="Enter Password", font=("Helvetica", 14), fg="white", bg="#2b2b2b").pack(pady=10)
entry = tk.Entry(root, show="*", font=("Helvetica", 14), width=25)
entry.pack(pady=5)

check_btn = tk.Button(root, text="Check Strength", command=check_password_strength, bg="#4a4a70", fg="white", font=("Helvetica", 12))
check_btn.pack(pady=15)

result_label = tk.Label(root, text="", font=("Helvetica", 12), fg="lightgreen", bg="#2b2b2b")
result_label.pack(pady=10)

root.mainloop()

import tkinter as tk
from tkinter import messagebox

def validate_login():
    username = username_entry.get()
    password = password_entry.get()

    # Check if username and password match a predefined set
    if username == "admin" and password == "password":
        messagebox.showinfo("Login Successful", "Welcome, " + username + "!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Create main window
root = tk.Tk()
root.title("Login Page")

# Create labels
username_label = tk.Label(root, text="Username:")
username_label.grid(row=0, column=0, padx=10, pady=5)
password_label = tk.Label(root, text="Password:")
password_label.grid(row=1, column=0, padx=10, pady=5)

# Create entry fields
username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1, padx=10, pady=5)
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=5)

# Create login button
login_button = tk.Button(root, text="Login", command=validate_login)
login_button.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

# Run the main event loop
root.mainloop()
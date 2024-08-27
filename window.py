import tkinter as tk
from tkinter import messagebox
import LocalAuthentication

# Create Main Window
root = tk.Tk()
root.title("Password Manager")
root.geometry("300x200")


# Create Login Window
def login():
    login_window = tk.Toplevel(root)
    login_window.title("Login")
    login_window.geometry("300x200")

    # Create a label
    label = tk.Label(login_window, text="Enter your password")
    label.pack()

    # Create a password entry
    password_entry = tk.Entry(login_window, show="*")
    password_entry.pack()

    # Create a submit button
    def submit():
        password = password_entry.get()
        if LocalAuthentication.authenticate(password):
            messagebox.showinfo("Success", "Login Successful")
        else:
            messagebox.showerror("Error", "Login Failed")

    submit_button = tk.Button(login_window, text="Submit", command=submit)
    submit_button.pack()
    login_window.mainloop()

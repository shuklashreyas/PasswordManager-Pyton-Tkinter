import tkinter as tk
from tkinter import messagebox, simpledialog


class PasswordManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Manager")
        self.root.geometry("400x300")

        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill="both", expand=True)

        self.show_login_screen()

    def clear_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def show_login_screen(self):
        self.clear_frame()

        tk.Label(self.main_frame, text="Username:").pack(pady=5)
        self.username_entry = tk.Entry(self.main_frame)
        self.username_entry.pack(pady=5)

        tk.Label(self.main_frame, text="Password:").pack(pady=5)
        self.password_entry = tk.Entry(self.main_frame, show="*")
        self.password_entry.pack(pady=5)

        tk.Button(self.main_frame, text="Login",
                  command=self.login).pack(pady=20)
        tk.Button(self.main_frame, text="Sign Up",
                  command=self.show_signup_screen).pack(pady=5)

    def show_signup_screen(self):
        self.clear_frame()

        tk.Label(self.main_frame, text="Create Username:").pack(pady=5)
        self.new_username_entry = tk.Entry(self.main_frame)
        self.new_username_entry.pack(pady=5)

        tk.Label(self.main_frame, text="Create Password:").pack(pady=5)
        self.new_password_entry = tk.Entry(self.main_frame, show="*")
        self.new_password_entry.pack(pady=5)

        tk.Button(self.main_frame, text="Sign Up",
                  command=self.sign_up).pack(pady=20)
        tk.Button(self.main_frame, text="Back to Login",
                  command=self.show_login_screen).pack(pady=5)

    def show_main_menu(self):
        self.clear_frame()

        tk.Button(self.main_frame, text="Add Password",
                  command=self.add_password).pack(pady=10)
        tk.Button(self.main_frame, text="View Passwords",
                  command=self.view_passwords).pack(pady=10)
        tk.Button(self.main_frame, text="Generate Random Password",
                  command=self.generate_random_password).pack(pady=10)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        # Replace with actual login logic
        if username == "admin" and password == "password123":
            messagebox.showinfo("Login Success", "Welcome!")
            self.show_main_menu()
        else:
            messagebox.showerror("Login Failed", "Invalid credentials")

    def sign_up(self):
        new_username = self.new_username_entry.get()
        # Replace with actual sign-up logic
        messagebox.showinfo("Sign Up Success",
                            f"Account created for {new_username}")
        self.show_login_screen()

    def add_password(self):
        # Logic for adding a password
        website = simpledialog.askstring("Website", "Enter the website name:")
        if website:
            messagebox.showinfo("Password Added",
                                f"Password for {website} added.")

    def view_passwords(self):
        # Logic for viewing passwords
        master_password = simpledialog.askstring("Master Password",
                                                 "Enter the master password:",
                                                 show='*')
        if master_password == "masterpass":  # Example master password
            messagebox.showinfo("Passwords", "Displaying all passwords...")
        else:
            messagebox.showerror("Error", "Invalid master password.")

    def generate_random_password(self):
        # Logic for generating random passwords
        random_password = "ABCD1234"
        messagebox.showinfo("Generated Password",
                            f"Your random password is: {random_password}")


if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordManagerApp(root)
    root.mainloop()

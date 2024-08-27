import tkinter as tk
from tkinter import ttk, simpledialog
from tkinter import messagebox
from user_manager import UserManager
from password_manager import PasswordManager


class PasswordManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Manager")
        self.root.geometry("800x500")
        self.root.configure(bg="#1c1c1c")

        self.user_manager = UserManager()
        self.password_manager = None
        self.current_user_id = None

        # Create a main frame
        self.main_frame = ttk.Frame(self.root, padding="20")
        self.main_frame.pack(fill="both", expand=True)

        # Initial login screen
        self.show_login_screen()

    def clear_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def show_login_screen(self):
        self.clear_frame()

        ttk.Label(self.main_frame, text="Login",
                  font=("Helvetica", 20, "bold"),
                  foreground="black").pack(pady=10)

        ttk.Label(self.main_frame, text="Username:",
                  foreground="black",
                  font=("Helvetica", 14)).pack(pady=5)
        self.username_entry = ttk.Entry(self.main_frame,
                                        font=("Helvetica", 14))
        self.username_entry.pack(pady=5)

        ttk.Label(self.main_frame, text="Password:",
                  foreground="black",
                  font=("Helvetica", 14)).pack(pady=5)
        self.password_entry = ttk.Entry(self.main_frame, show="*",
                                        font=("Helvetica", 14))
        self.password_entry.pack(pady=5)

        ttk.Button(self.main_frame, text="Login",
                   command=self.login, style="Accent.TButton",
                   padding=(10, 5)).pack(pady=20)
        ttk.Button(self.main_frame, text="Sign Up",
                   command=self.show_signup_screen).pack(pady=5)

    def show_signup_screen(self):
        self.clear_frame()

        ttk.Label(self.main_frame, text="Sign Up",
                  font=("Helvetica", 20, "bold"),
                  background="#1c1c1c", foreground="white").pack(pady=10)

        ttk.Label(self.main_frame, text="Create Username:",
                  background="#1c1c1c", foreground="white",
                  font=("Helvetica", 14)).pack(pady=5)
        self.new_username_entry = ttk.Entry(self.main_frame,
                                            font=("Helvetica", 14))
        self.new_username_entry.pack(pady=5)

        ttk.Label(self.main_frame, text="Create Password:",
                  background="#1c1c1c", foreground="white",
                  font=("Helvetica", 14)).pack(pady=5)
        self.new_password_entry = ttk.Entry(self.main_frame, show="*",
                                            font=("Helvetica", 14))
        self.new_password_entry.pack(pady=5)

        ttk.Button(self.main_frame, text="Sign Up",
                   command=self.sign_up, style="Accent.TButton",
                   padding=(10, 5)).pack(pady=20)
        ttk.Button(self.main_frame, text="Back to Login",
                   command=self.show_login_screen).pack(pady=5)

    def show_main_menu(self):
        self.clear_frame()

        ttk.Label(self.main_frame, text="Main Menu",
                  font=("Helvetica", 20, "bold"),
                  foreground="black").pack(pady=10)

        ttk.Button(self.main_frame, text="Add Password",
                   command=self.add_password, style="Accent.TButton",
                   padding=(10, 5)).pack(pady=10)
        ttk.Button(self.main_frame, text="View Passwords",
                   command=self.view_passwords, style="Accent.TButton",
                   padding=(10, 5)).pack(pady=10)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        user_id = self.user_manager.login(username, password)
        if user_id:
            self.current_user_id = user_id
            self.password_manager = PasswordManager(user_id)
            self.show_main_menu()
        else:
            messagebox.showerror("Login Failed", "Invalid credentials")

    def sign_up(self):
        new_username = self.new_username_entry.get()
        new_password = self.new_password_entry.get()

        if self.user_manager.sign_up(new_username, new_password):
            messagebox.showinfo("Success", "Account created successfully")
            self.show_login_screen()
        else:
            messagebox.showerror("Sign Up Failed", "Username already exists")

    def add_password(self):
        website = simpledialog.askstring("Website", "Enter the website name:")
        username = simpledialog.askstring("Username", "Enter the username:")
        password = simpledialog.askstring("Password", "Enter the password:")

        if website and username and password:
            self.password_manager.add_password(website, username, password)

    def view_passwords(self):
        self.password_manager.view_passwords()


if __name__ == "__main__":
    root = tk.Tk()

    # Set a modern theme for the ttk widgets
    style = ttk.Style(root)
    style.theme_use("clam")  # Using a built-in theme

    app = PasswordManagerApp(root)
    root.mainloop()

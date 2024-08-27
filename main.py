import tkinter as tk
from tkinter import simpledialog
from PIL import Image, ImageTk
from user_manager import UserManager
from password_manager import PasswordManager


class PasswordManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Manager")
        self.root.geometry("600x400")

        self.user_manager = UserManager()
        self.password_manager = None
        self.current_user_id = None

        # Load the background image
        self.background_image = Image.open("background.jpg")
        self.background_photo = ImageTk.PhotoImage(self.background_image)

        # Create a Label widget to display the background image
        self.background_label = tk.Label(self.root,
                                         image=self.background_photo)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Create a frame on top of the background image
        self.main_frame = tk.Frame(self.root,
                                   bg='#333333', bd=5)
        self.main_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Initial login screen
        self.show_login_screen()

    def clear_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def show_login_screen(self):
        self.clear_frame()
        tk.Label(self.main_frame, text="Username:",
                 bg='#333333', fg='white').pack(pady=5)
        self.username_entry = tk.Entry(self.main_frame)
        self.username_entry.pack(pady=5)

        tk.Label(self.main_frame, text="Password:", bg='#333333',
                 fg='white').pack(pady=5)
        self.password_entry = tk.Entry(self.main_frame, show="*")
        self.password_entry.pack(pady=5)

        tk.Button(self.main_frame, text="Login",
                  command=self.login).pack(pady=20)
        tk.Button(self.main_frame, text="Sign Up",
                  command=self.show_signup_screen).pack(pady=5)

    def show_signup_screen(self):
        self.clear_frame()

        tk.Label(self.main_frame, text="Create Username:",
                 bg='#333333', fg='white').pack(pady=5)
        self.new_username_entry = tk.Entry(self.main_frame)
        self.new_username_entry.pack(pady=5)

        tk.Label(self.main_frame, text="Create Password:",
                 bg='#333333', fg='white').pack(pady=5)
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

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        user_id = self.user_manager.login(username, password)
        if user_id:
            self.current_user_id = user_id
            self.password_manager = PasswordManager(user_id)
            self.show_main_menu()

    def sign_up(self):
        new_username = self.new_username_entry.get()
        new_password = self.new_password_entry.get()

        if self.user_manager.sign_up(new_username, new_password):
            self.show_login_screen()

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
    app = PasswordManagerApp(root)
    root.mainloop()

import tkinter as tk
from tkinter import messagebox, simpledialog
from PIL import Image, ImageTk
import sqlite3


class PasswordManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Manager")
        self.root.geometry("600x400")
        
        self.current_user_id = None  # To track logged-in user

        # Initialize SQLite database
        self.initialize_db()

        # Load the background image
        self.background_image = Image.open("background.jpg") 
        self.background_photo = ImageTk.PhotoImage(self.background_image)

        # Create a Label widget to display the background image
        self.background_label = tk.Label(self.root,
                                         image=self.background_photo)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Create a frame on top of the background image
        self.main_frame = tk.Frame(self.root, bg='#333333', bd=5)  # Dark
        # background frame
        self.main_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Add widgets to the frame (on top of the background)
        tk.Label(self.main_frame, text="Username:", bg='#333333',
                 fg='white').pack(pady=5)
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

    def initialize_db(self):
        conn = sqlite3.connect('password_manager.db')
        c = conn.cursor()
        
        c.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL
            )
        ''')
        
        c.execute('''
            CREATE TABLE IF NOT EXISTS passwords (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                website TEXT NOT NULL,
                username TEXT NOT NULL,
                password TEXT NOT NULL,
                user_id INTEGER,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        ''')
        
        conn.commit()
        conn.close()

    def clear_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def show_login_screen(self):
        self.clear_frame()
        tk.Label(self.main_frame, text="Username:",
                 bg='#333333', fg='white').pack(pady=5)
        self.username_entry = tk.Entry(self.main_frame)
        self.username_entry.pack(pady=5)

        tk.Label(self.main_frame, text="Password:",
                 bg='#333333', fg='white').pack(pady=5)
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
        tk.Button(self.main_frame, text="Generate Random Password",
                  command=self.generate_random_password).pack(pady=10)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        conn = sqlite3.connect('password_manager.db')
        c = conn.cursor()
        
        c.execute('SELECT id FROM users WHERE username = ? AND password = ?',
                  (username, password))
        user = c.fetchone()
        
        if user:
            self.current_user_id = user[0]
            messagebox.showinfo("Login Success", "Welcome!")
            self.show_main_menu()
        else:
            messagebox.showerror("Login Failed", "Invalid credentials")
        
        conn.close()

    def sign_up(self):
        new_username = self.new_username_entry.get()
        new_password = self.new_password_entry.get()
        
        conn = sqlite3.connect('password_manager.db')
        c = conn.cursor()
        
        try:
            c.execute('INSERT INTO users (username, password) VALUES (?, ?)', 
                      (new_username, new_password))
            conn.commit()
            messagebox.showinfo("Sign Up Success",
                                f"Account created for {new_username}")
            self.show_login_screen()
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Username already exists.")
        
        conn.close()

    def add_password(self):
        website = simpledialog.askstring("Website", "Enter the website name:")
        username = simpledialog.askstring("Username", "Enter the username:")
        password = simpledialog.askstring("Password", "Enter the password:")
        
        if website and username and password:
            conn = sqlite3.connect('password_manager.db')
            c = conn.cursor()
            
            c.execute('''
                INSERT INTO passwords (website, username, password, user_id)
                VALUES (?, ?, ?, ?)
            ''', (website, username, password, self.current_user_id))
            
            conn.commit()
            conn.close()
            
            messagebox.showinfo("Success", f"Password for {website} added!")

    def view_passwords(self):
        master_password = simpledialog.askstring("Master Password",
                                                 "Enter the master password:",
                                                 show='*')
        
        if master_password == "masterpass":
            conn = sqlite3.connect('password_manager.db')
            c = conn.cursor()
            
            c.execute(
                'SELECT website, user_id = ?',
                (self.current_user_id,)
            )
            passwords = c.fetchall()
            
            conn.close()
            
            if passwords:
                for pw in passwords:
                    messagebox.showinfo(f"Password for {pw[0]}",
                                        (f"Username: {pw[1]}\n"
                                         f"Password: {pw[2]}"))
            else:
                messagebox.showinfo("Info", "No passwords stored.")
        else:
            messagebox.showerror("Error", "Invalid master password.")

    def generate_random_password(self):
        random_password = "ABCD1234" 
        messagebox.showinfo("Generated Password",
                            f"Your random password is: {random_password}")


if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordManagerApp(root)
    root.mainloop()

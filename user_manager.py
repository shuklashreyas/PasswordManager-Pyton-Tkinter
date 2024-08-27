import sqlite3
from tkinter import messagebox


class UserManager:
    def __init__(self, db_name='password_manager.db'):
        self.db_name = db_name
        self.initialize_db()

    def initialize_db(self):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()

        c.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL
            )
        ''')

        conn.commit()
        conn.close()

    def sign_up(self, username, password):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()

        try:
            c.execute('INSERT INTO users (username, password) VALUES (?, ?)',
                      (username, password))
            conn.commit()
            messagebox.showinfo("Sign Up Success",
                                f"Account created for {username}")
            success = True
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Username already exists.")
            success = False

        conn.close()
        return success

    def login(self, username, password):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()

        c.execute('SELECT id FROM users WHERE username = ? AND password = ?',
                  (username, password))
        user = c.fetchone()

        conn.close()

        if user:
            return user[0]  # Returning the user ID
        else:
            messagebox.showerror("Login Failed", "Invalid credentials")
            return None

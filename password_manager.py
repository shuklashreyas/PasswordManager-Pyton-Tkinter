import sqlite3
from tkinter import messagebox, simpledialog


class PasswordManager:
    def __init__(self, user_id, db_name='password_manager.db'):
        self.user_id = user_id
        self.db_name = db_name
        self.initialize_db()

    def initialize_db(self):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()

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

    def add_password(self, website, username, password):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()

        c.execute('''
            INSERT INTO passwords (website, username, password, user_id)
            VALUES (?, ?, ?, ?)
        ''', (website, username, password, self.user_id))

        conn.commit()
        conn.close()

        messagebox.showinfo("Success", f"Password for {website} added!")

    def view_passwords(self):
        master_password = simpledialog.askstring(
            "Master Password", "Enter the master password:", show='*'
        )

        if master_password == "masterpass":
            conn = sqlite3.connect(self.db_name)
            c = conn.cursor()

            c.execute(
                ('SELECT website, username, password FROM passwords '
                 'WHERE user_id = ?'),
                (self.user_id,)
            )
            passwords = c.fetchall()

            conn.close()

            if passwords:
                for pw in passwords:
                    messagebox.showinfo(
                        f"Password for {pw[0]}",
                        f"Username: {pw[1]}\nPassword: {pw[2]}"
                    )
            else:
                messagebox.showinfo("Info", "No passwords stored.")
        else:
            messagebox.showerror("Error", "Invalid master password.")
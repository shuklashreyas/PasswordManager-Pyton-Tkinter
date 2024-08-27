import sqlite3
from tkinter import messagebox, Tk, Toplevel
from tkinter.ttk import Treeview
import LocalAuthentication
from LocalAuthentication import LAPolicyDeviceOwnerAuthenticationWithBiometrics


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

    def authenticate_with_touch_id(self, on_success, on_failure):
        context = LocalAuthentication.LAContext.alloc().init()
        reason = "Authenticate to view your passwords"

        def callback(success, error):
            if success:
                on_success()
            else:
                on_failure(error)

        context.evaluatePolicy_localizedReason_reply_(
            LAPolicyDeviceOwnerAuthenticationWithBiometrics,
            reason,
            callback
        )

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
        def on_success():
            conn = sqlite3.connect(self.db_name)
            c = conn.cursor()

            c.execute(
                ('SELECT website, password FROM passwords '
                 'WHERE user_id = ?'),
                (self.user_id,)
            )
            passwords = c.fetchall()

            conn.close()

            if passwords:
                # Create a new window to display the passwords
                window = Toplevel()
                window.title("Stored Passwords")

                # Create the Treeview
                tree = Treeview(window, columns=("Website", "Password"),
                                show="headings")
                tree.heading("Website", text="Website")
                tree.heading("Password", text="Password")

                # Insert the data into the Treeview
                for pw in passwords:
                    tree.insert("", "end", values=pw)

                tree.pack(fill="both", expand=True)
            else:
                messagebox.showinfo("Info", "No passwords stored.")

        def on_failure(error):
            messagebox.showerror(
                "Authentication Failed",
                "Touch ID authentication failed."
            )

        self.authenticate_with_touch_id(on_success, on_failure)


# Example usage
if __name__ == "__main__":
    root = Tk()
    root.withdraw()  # Hide the root window
    manager = PasswordManager(user_id=1)  # Replace with actual user_id
    manager.view_passwords()
    root.mainloop()

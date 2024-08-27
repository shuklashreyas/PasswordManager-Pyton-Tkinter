import sqlite3
import hashlib

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('users.db')
c = conn.cursor()

# Create a table to store user credentials
c.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
''')


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def sign_up(username, password):
    hashed_password = hash_password(password)
    try:
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)",
                  (username, hashed_password))
        conn.commit()
        print("User signed up successfully.")
    except sqlite3.IntegrityError:
        print("Username already exists.")


def log_in(username, password):
    hashed_password = hash_password(password)
    c.execute("SELECT * FROM users WHERE username = ? AND password = ?",
              (username, hashed_password))
    user = c.fetchone()
    if user:
        print("Login successful.")
        return True
    else:
        print("Login failed.")
        return False


# Example usage
sign_up('user1', 'password123')
log_in('user1', 'password123')

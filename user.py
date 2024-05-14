import sqlite3
import hashlib

DATABASE_FILE = 'users.db'

def create_user_table():
    """Create the users table if it doesn't exist."""
    conn = sqlite3.connect(DATABASE_FILE)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    username TEXT NOT NULL UNIQUE,
                    hashed_password TEXT NOT NULL
                )''')
    conn.commit()
    conn.close()

def add_user(username, hashed_password):
    """Add a new user to the database."""
    conn = sqlite3.connect(DATABASE_FILE)
    c = conn.cursor()
    password = hashlib.sha256(hashed_password.encode()).hexdigest()
    c.execute('INSERT INTO users (username, hashed_password) VALUES (?, ?)', (username, password))
    conn.commit()
    conn.close()

def verify_user(username, password):
    """Verify if the username and password match."""
    conn = sqlite3.connect(DATABASE_FILE)
    c = conn.cursor()
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    c.execute('SELECT * FROM users WHERE username = ? AND hashed_password = ?', (username, hashed_password))
    user = c.fetchone()
    conn.close()
    return user is not None

def delete_user(username):
    """Delete a user from the database."""
    conn = sqlite3.connect(DATABASE_FILE)
    c = conn.cursor()
    c.execute('DELETE FROM users WHERE username = ?', (username,))
    conn.commit()
    conn.close()

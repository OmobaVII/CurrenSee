import tkinter as tk
from tkinter import ttk, messagebox
from user import add_user

class RegPage(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.title("Register")
        self.geometry("300x200")
        self.iconbitmap("images/icon.ico")
        
        self.label_fullname = ttk.Label(self, text="Full Name:")
        self.label_username = ttk.Label(self, text="Username:")
        self.label_password = ttk.Label(self, text="Password:")
        
        self.entry_fullname = ttk.Entry(self)
        self.entry_username = ttk.Entry(self)
        self.entry_password = ttk.Entry(self, show="*")
        
        self.button_register = ttk.Button(self, text="Register", command=self.register)
        
        self.label_fullname.grid(row=0, column=0, padx=5, pady=5)
        self.entry_fullname.grid(row=0, column=1, padx=5, pady=5)
        self.label_username.grid(row=1, column=0, padx=5, pady=5)
        self.entry_username.grid(row=1, column=1, padx=5, pady=5)
        self.label_password.grid(row=2, column=0, padx=5, pady=5)
        self.entry_password.grid(row=2, column=1, padx=5, pady=5)
        self.button_register.grid(row=3, columnspan=2, padx=7, pady=5)

    def register(self):
        fullname = self.entry_fullname.get()
        username = self.entry_username.get()
        password = self.entry_password.get()

        if fullname and username and password:
            try:
                add_user(username, password)
                messagebox.showinfo("Success", "User created successfully")
                self.parent.deiconify()  # Show main window
                self.destroy()  # Close registration window
            except:
                messagebox.showerror("Error", "Username already exists")
        else:
            messagebox.showerror("Error", "Please fill in all fields")

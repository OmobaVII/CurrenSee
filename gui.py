import tkinter
from tkinter import Label, Entry, StringVar, Button, PhotoImage, ttk, messagebox
from ttkwidgets.autocomplete import AutocompleteCombobox
from datetime import datetime
import webbrowser
from user import verify_user, create_user_table
from Reg_page import RegPage
from validation_conversion import  validate_input, currency_values
from currency_convert import convert_currency



class LoginPage(tkinter.Toplevel):
    def __init__(self, parent, main_page_ref):
        super().__init__(parent)
        self.parent = parent
        self.main_page_ref = main_page_ref
        self.title("Login")
        self.geometry("300x150")
        self.iconbitmap("images/icon.ico")
        
        self.label_username = ttk.Label(self, text="Username:")
        self.label_password = ttk.Label(self, text="Password:")
        
        self.entry_username = ttk.Entry(self)
        self.entry_password = ttk.Entry(self, show="*")
        
        self.button_login = ttk.Button(self, text="Login", command=self.login)
        self.button_reg = ttk.Button(self, text="Register", command=self.register)
        
        self.label_username.grid(row=0, column=0, padx=5, pady=5)
        self.label_password.grid(row=1, column=0, padx=5, pady=5)
        self.entry_username.grid(row=0, column=1, padx=5, pady=5)
        self.entry_password.grid(row=1, column=1, padx=5, pady=5)
        self.button_login.grid(row=2, columnspan=2, padx=5, pady=5)

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        if verify_user(username, password):
            messagebox.showinfo("Success", "Login successful")
            #self.parent.withdraw()
            self.parent.open_main_page(username)
            self.destroy()
        else:
            messagebox.showerror("Error", "Invalid username or password")
        

class MainPage(tkinter.Toplevel):
    def __init__(self, parent, username):
        size = 10
        super().__init__(parent)
        self.title("CurrenSee")
        self.geometry("700x200")
        self.resizable(False, False)
        self.iconbitmap("images/icon.ico")
        self.background_image = PhotoImage(file="images/background2.png")
        self.button_convert_img = PhotoImage(file="images/Convert.png")
        self.button_convert_img_sampled = self.button_convert_img.subsample(size, size)
        self.username = username
        self.create_widgets()

    def create_widgets(self):
        label_font = ("Helvetica", 16)
        date_font = ("Times New Roman", 8)
        foreground = "blue"
        size = 10

        # Labels
        label_amount = Label(self, text="FROM", font=label_font, foreground="blue")
        label_target_currency = Label(self, text="TO", font=label_font, foreground="blue")
        label_result = Label(self, text="Converted Amount:", font=label_font, foreground="red")
        label_date = Label(self, font=date_font, foreground="red", bg=self["bg"])
        
        background_label = Label(self, image=self.background_image)

        # Function to write a default amount
        def amount_entry(event):
            """function to use if the amount section is active"""
            if entry_amount.get() == "Enter Amount":
                entry_amount.delete(0, "end")
                entry_amount.config(foreground="black")

        def amount_leave(event):
            """function to use if amount is not active"""
            if not entry_amount.get():
                entry_amount.insert(0, "Enter Amount")
                entry_amount.config(foreground="grey")

        # Function to perform currency conversion
        def perform_conversion():
            """performs the conversion"""
            amount_str = entry_amount.get()
            error_message = validate_input(amount_str)

            if error_message:
                label_result.config(text=error_message)
            else:
                try:
                    amount = float(amount_str)
                    base_currency = dropdown_base_currency.get()
                    target_currency = dropdown_target_currency.get()
                    if base_currency == "Select Base Currency":
                        label_result.config(text="Select a Base Currency")
                        return
                    if target_currency == "Select Target Currency":
                        label_result.config(text="Select a Target Currency")
                        return
                    result = convert_currency(amount, base_currency, target_currency)
                    converted_amount = result[0]
                    last_update = datetime.strptime(result[1], "%Y-%m-%dT%H:%M:%SZ")

                    if converted_amount != -1:
                        label_result.config(text=f"{converted_amount:.2f} {target_currency}")
                        label_date.config(text=f"Last Updated at: {last_update}")
                    else:
                        label_result.config(text="Error fetching exchange rates")
                except Exception as e:
                    label_result.config(text="Check your internet connection")
        # Entry Fields
        entry_amount = Entry(self, font=label_font)
        entry_amount.insert(0, "Enter Amount")
        entry_amount.bind("<FocusIn>", amount_entry)
        entry_amount.bind("<FocusOut>", amount_leave)

        # Dropdown Menus (for currency selection)
        base_currency_var = StringVar(self)
        base_currency_var.set("Select Base Currency")
        dropdown_base_currency = AutocompleteCombobox(self, font=label_font, foreground=foreground)
        dropdown_base_currency["values"] = currency_values
        dropdown_base_currency["state"] = "readonly"
        dropdown_base_currency.set("Select Base Currency")

        target_currency_var = StringVar(self)
        target_currency_var.set("Select Target Currency")
        dropdown_target_currency = AutocompleteCombobox(self, font=label_font, foreground=foreground)
        dropdown_target_currency["values"] = currency_values
        dropdown_target_currency["state"] = "readonly"
        dropdown_target_currency.set("Select Target Currency")

        # Create a styled "Convert" button using ttk
        button_convert = Button(self, image=self.button_convert_img_sampled, borderwidth=0, command=perform_conversion, highlightthickness=0, bg=self["bg"])

        label_welcome = Label(self, font=label_font, foreground="red", bg=self.cget("background"))
        label_welcome.config(text=f"Welcome {self.username}")
        # THE ARCHITECTURE OF THE GUI
        for i in range(3):
            self.columnconfigure(i, weight=20, minsize=20)

        background_label.place(x=0, y=0, relwidth=1, relheight=1) 
        label_result.lift()
        label_date.lift()
        label_amount.grid(row=0, column=0)
        dropdown_base_currency.grid(row=1, column=0)
        entry_amount.grid(row=2, column=0)

        label_target_currency.grid(row=0, column=1)
        label_welcome.grid(row=0, column=0, columnspan=4)
        dropdown_target_currency.grid(row=1, column=1)
        label_result.grid(row=2, column=1)
        label_date.grid(row=3, column=0, columnspan=2)
        button_convert.grid(row=0, column=2, rowspan=3, padx=10, pady=10)

class App(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title("CurrenSee")
        self.geometry("700x200")
        self.resizable(False, False)
        self.iconbitmap("images/icon.ico")
        self.background_image = PhotoImage(file="images/background2.png")
        background_label = Label(self, image=self.background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1) 
        self.create_widgets()
        create_user_table()

    def create_widgets(self):
        label_font = ("Helvetica", 16)
        date_font = ("Times New Roman", 8)
        foreground = "blue"
        button_show_login = tkinter.Button(self, text="Login", background="white", font=label_font, command=self.show_login_page)
        button_show_register = tkinter.Button(self, text="Register", background="white", font=label_font, command=self.show_register_page)
        button_show_login.pack(side="left", padx=10)
        button_show_register.pack(side="left", padx=10)

    def show_login_page(self):
        self.withdraw()  
        login_window = LoginPage(self, self)
        login_window.grab_set()

    def show_register_page(self):
        self.withdraw()  
        register_window = RegPage(self)

    def open_main_page(self, username):
        main_page = MainPage(self, username)
    

if __name__ == "__main__":
    app = App()
    app.mainloop()
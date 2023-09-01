#!/bin/usr/python3
"""
This module designs the GUI of the CurrenSee
"""
import tkinter
from tkinter import Label, Entry, StringVar
from tkinter import Button, ttk, PhotoImage, Listbox
from currency_convert import convert_currency
from validation_conversion import validate_input, currency_values
from ttkwidgets.autocomplete import AutocompleteCombobox
from datetime import datetime
import webbrowser


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

# Function to create clickable banner
def hire_me():
    """function to click hire me to github"""
    webbrowser.open_new_tab("https://github.com/OmobaVII")

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


root = tkinter.Tk()
root.title("CurrenSee")
root.geometry("700x200")
root.iconbitmap("images/icon.ico")
# root.configure(bg="blue")

background_image = PhotoImage(file="images/background2.png")


label_font = ("Helvetica", 16)
date_font = ("Times New Roman", 8)
foreground = ("blue")
size = 10

#Labels
label_amount = Label(root, text="FROM", font=label_font, foreground="blue")
label_target_currency = Label(root, text="TO", font=label_font, foreground="blue")
label_result = Label(root, text="Converted Amount:", font=label_font, foreground="red")
label_date = Label(root, font=date_font, foreground="red", bg=root["bg"])    
background_label = Label(root, image=background_image)
background_label.place(x=0, y=0)

#Entry Fields
entry_amount = Entry(root, font=label_font)
entry_amount.insert(0, "Enter Amount")
entry_amount.bind("<FocusIn>", amount_entry)
entry_amount.bind("<FocusOut>", amount_leave)

# Dropdown Menus (for currency selection)
base_currency_var = StringVar(root)
base_currency_var.set("Select Base Currency")  # My Default currency
dropdown_base_currency = AutocompleteCombobox(root, font=label_font, foreground=foreground)
dropdown_base_currency["values"] = currency_values
dropdown_base_currency["state"] = "readonly"  # Make it readonly
dropdown_base_currency.set("Select Base Currency")
dropdown_base_currency.config(font=label_font, foreground=foreground)

target_currency_var = StringVar(root)
target_currency_var.set("Select Target Currency")  # My Default currency
dropdown_target_currency = AutocompleteCombobox(root, font=label_font, foreground=foreground)
dropdown_target_currency["values"] = currency_values
dropdown_target_currency["state"] = "readonly"  # Make it readonly
dropdown_target_currency.set("Select Target Currency")
dropdown_target_currency.config(font=label_font, foreground=foreground)

# Create a styled "Convert" button using ttk
button_convert_img = PhotoImage(file="images/Convert.png") 
button_convert_img = button_convert_img.subsample(size, size)
button_convert = Button(root, image = button_convert_img, borderwidth = 0, command=perform_conversion,
                        highlightthickness=0, bg=root["bg"])

hireme = PhotoImage(file="images/Hire_me_Banner.png")
hireme = hireme.subsample(size, size)
label_hire_me = Button(root, image=hireme, cursor="hand2", command = hire_me, bg=root["bg"])


# THE ARCHITECTURE OF THE GUI
for i in range(3):
    root.columnconfigure(i, weight=20, minsize=20)

background_label.place(x=0, y=0, relwidth=1, relheight=1) 
label_result.lift()
label_date.lift()
label_amount.grid(row=0, column=0)
dropdown_base_currency.grid(row=1, column=0)
entry_amount.grid(row=2, column=0)

label_target_currency.grid(row=0, column=1)
dropdown_target_currency.grid(row=1, column=1)
label_result.grid(row=2, column=1)
label_date.grid(row=3, column=0, columnspan=2)
button_convert.grid(row=0, column=2, rowspan=3, padx=10, pady=10)
label_hire_me.grid(row=4, column=2, columnspan=3)

if __name__ == "__main__":
    root.mainloop()
from tkinter import *
import pandas as pd
import os
from datetime import datetime


categories = ["Food", "Rent", "Shopping", "Utilities", "Transport", "Others"]
df_transaction = pd.DataFrame(columns=["Category", "Amount", "Timestamp"])
df_income = pd.DataFrame(columns=["Income", "Month", "Timestamp"])


def register():
    """Handles user registration."""
    global username
    user_name = entry_name.get()
    user_email = entry_email.get()
    user_password = entry_password.get()

    username = user_email.split("@")[0]

    new_data = pd.DataFrame({
        "timestamp": [datetime.now().strftime("%d|%m|%Y %H:%M:%S")],
        "name": [user_name],
        "email": [user_email],
        "password": [user_password]
    })

    if os.path.exists("result.csv"):
        new_data.to_csv('result.csv', mode='a', index=False, header=False)
    else:
        new_data.to_csv('result.csv', mode='w', index=False, header=True)

    label_output.config(
        text=f"User registered successfully! Your username is '{username}'", fg="green"
    )

    go_to_main_page()


def go_to_main_page():
    """Displays the main page with options for adding transactions or income."""
    for widget in root.winfo_children():
        widget.destroy()

    Label(root, text="Main Page", font=("Times New Roman", 18, "bold"), fg="blue").pack(pady=10)
    Label(root, text=f"Welcome, {username}!", font=("Times New Roman", 14)).pack(pady=10)

    Button(root, text="Add Transaction", command=go_to_transaction_page, fg="white", bg="green", font=("Times New Roman", 18)).pack(pady=20)
    Button(root, text="Add Income", command=go_to_income_page, fg="white", bg="blue", font=("Times New Roman", 18)).pack(pady=20)


def go_to_transaction_page():
    """Navigates to the transaction page."""
    for widget in root.winfo_children():
        widget.destroy()

    Label(root, text="Transaction Page", font=("Times New Roman", 18, "bold"), fg="blue").pack(pady=10)
    Label(root, text="Enter Transaction Details:", font=("Times New Roman", 12)).pack(pady=10)

    global category_var
    category_var = StringVar()
    category_var.set("Select Category")
    Label(root, text="Category:").pack()
    dropdown = OptionMenu(root, category_var, *categories)
    dropdown.pack()

    Label(root, text="Amount:").pack()
    global entry_amount
    entry_amount = Entry(root, width=50, font=("Times New Roman", 18))
    entry_amount.pack()

    Button(root, text="Add Transaction", command=add_transaction, fg="white", bg="green", font=("Times New Roman", 18)).pack(pady=20)

    global transaction_output
    transaction_output = Label(root, text="", font=("Times New Roman", 18))
    transaction_output.pack()


def go_to_income_page():
    """Navigates to the income page."""
    for widget in root.winfo_children():
        widget.destroy()

    Label(root, text="Income Page", font=("Times New Roman", 18, "bold"), fg="blue").pack(pady=10)
    Label(root, text="Enter Monthly Income:", font=("Times New Roman", 12)).pack(pady=10)

    Label(root, text="Income Amount:").pack()
    global entry_income
    entry_income = Entry(root, width=50, font=("Times New Roman", 18))
    entry_income.pack()

    Button(root, text="Add Income", command=add_income, fg="white", bg="blue", font=("Times New Roman", 18)).pack(pady=20)

    global income_output
    income_output = Label(root, text="", font=("Times New Roman", 18))
    income_output.pack()


def add_transaction():
    """Handles adding a transaction."""
    global df_transaction
    category = category_var.get()
    amount = entry_amount.get()

    if category != "Select Category" and amount:
        try:
            amount = float(amount)
            transaction_output.config(text=f"Transaction added: {category} - ₹{amount:.2f}", fg="green")

            # Add transaction
            new_row = {
                "Category": category,
                "Amount": amount,
                "Timestamp": datetime.now().strftime("%d|%m|%Y %H:%M:%S")
            }
            df_transaction = pd.concat([df_transaction, pd.DataFrame([new_row])], ignore_index=True)
            df_transaction.to_csv(f"{username}_transactions.csv", index=False)
        except ValueError:
            transaction_output.config(text="Invalid amount! Please enter a number.", fg="red")
    else:
        transaction_output.config(text="Please fill out all fields.", fg="red")


def add_income():
    """Handles adding income for the user."""
    global df_income
    income = entry_income.get()
    current_month = datetime.now().strftime("%B")

    if income:
        try:
            income = float(income)
            if os.path.exists(f"{username}_income.csv"):
                df_income = pd.read_csv(f"{username}_income.csv")
                if current_month in df_income["Month"].values:
                    income_output.config(text="Income for this month already added!", fg="red")
                    return
            else:
                df_income = pd.DataFrame(columns=["Income", "Month", "Timestamp"])

            # Add income
            new_row = {
                "Income": income,
                "Month": current_month,
                "Timestamp": datetime.now().strftime("%d|%m|%Y %H:%M:%S")
            }
            df_income = pd.concat([df_income, pd.DataFrame([new_row])], ignore_index=True)
            df_income.to_csv(f"{username}_income.csv", index=False)
            income_output.config(text=f"Income added for {current_month}: ₹{income:.2f}", fg="green")
        except ValueError:
            income_output.config(text="Invalid amount! Please enter a number.", fg="red")
    else:
        income_output.config(text="Please fill out the income field.", fg="red")


# Main Application
root = Tk()
root.title("PERSONAL FINANCE MANAGER")

Label(root, text="PERSONAL FINANCE TRACKER", font=("Times New Roman", 28, "bold"), fg="blue").pack(pady=20)
Label(root, text="Register User", font=("Times New Roman", 18, "bold")).pack(pady=10)

Label(root, text="Name:").pack()
entry_name = Entry(root, width=50, font=("Times New Roman", 18))
entry_name.pack()

Label(root, text="Email:").pack()
entry_email = Entry(root, width=50, font=("Times New Roman", 18))
entry_email.pack()

Label(root, text="Password:").pack()
entry_password = Entry(root, width=50, show="*", font=("Times New Roman", 18))
entry_password.pack()

Button(root, text="Register", command=register, fg="white", bg="green", font=("Times New Roman", 12)).pack(pady=20)

label_output = Label(root, text="", fg="green", font=("Times New Roman", 18))
label_output.pack()

root.mainloop()

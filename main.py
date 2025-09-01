# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import pyperclip
import random
import json
from tkinter import *
from tkinter import messagebox


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]

    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)

    password = "".join(password_list)
    pass_entry.delete(0, END)
    pass_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def saving_data():
    email = email_name_entry.get()
    password = pass_entry.get()
    website = website_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(email) == 0 or len(password) == 0 or len(website) == 0:
        messagebox.showinfo(title="Try again", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            data = {}
        except json.JSONDecodeError:
            data = {}

        data.update(new_data)

        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)

        website_entry.delete(0, END)
        pass_entry.delete(0, END)


# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search_for_data():
    name_of_website = website_entry.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo("Error", "No Data File Found.")
    except json.JSONDecodeError:
        messagebox.showinfo("Error", "Data file is empty or corrupted.")
    else:
        if name_of_website in data:
            email = data[name_of_website]["email"]
            password = data[name_of_website]["password"]
            messagebox.showinfo("Your Data", message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo("Not Found", f"No details for '{name_of_website}' found.")


# ---------------------------- UI SETUP ------------------------------- #
win = Tk()
win.title("Password Manager")
win.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
photo_image = PhotoImage(file=r"logo.png")
canvas.create_image(100, 100, image=photo_image)
canvas.grid(row=0, column=1)

# Website label
web_label = Label(text="Website:")
web_label.grid(row=1, column=0)

# Website entry
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)

# Search button
search = Button(text="Search", width=10, command=search_for_data)
search.grid(row=1, column=3)

# Email label
email_label = Label(text="Email/Name:")
email_label.grid(row=2, column=0)

# Email and username entry
email_name_entry = Entry(width=35)
email_name_entry.grid(row=2, column=1, columnspan=2)

# Password label
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Password entry
pass_entry = Entry(width=21)
pass_entry.grid(row=3, column=1)

# Generate password button
gen_pass = Button(text="Generate", command=generate_password)
gen_pass.grid(row=3, column=2)

# Add password button
add_button = Button(text="Add", width=36, command=saving_data)
add_button.grid(row=4, column=1, columnspan=2)

win.mainloop()

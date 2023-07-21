# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import pyperclip
import random
import json
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)


    password_letters = [random.choice(letters) for char in range(nr_letters)]
    password_numbers = [random.choice(numbers) for char in range(nr_numbers)]
    password_symbols = [random.choice(symbols) for char in range(nr_symbols)]

    password_list = password_letters + password_numbers + password_symbols


    random.shuffle(password_list)
    password = "".join(password_list)
    pass_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

from tkinter import *
from tkinter import messagebox

win = Tk()

win.title("Passoward Manager")
win.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)

photo_image = PhotoImage(file=r"logo.png")
canvas.create_image(100, 100, image=photo_image)
canvas.grid(row=0, column=1)


def search_for_data():
    name_of_website = website_entry.get()
    with open(r"data.json", "r") as file:
        data = json.load(file)
        if name_of_website in data:
            email = data[name_of_website]["email"]
            password = data[name_of_website]["password"]
            messagebox.showinfo("Your Data", message=f"email={email}\npassword={password}")





def saving_data():
    email = email_name_entry.get()
    passoward = pass_entry.get()
    website = website_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": passoward,
        }
    }
    if len(email) == 0 or len(passoward) == 0 or len(website) == 0:
        messagebox.showinfo(title="try again", message="Please don't leave any fields empty!")

    else:
        try:
            with open(r"data.json", "r") as file:
                #reading data
                data = json.load(file)
        except FileNotFoundError:
            with open(r"data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:

            #updating new data with new data
            data.update(new_data)
            with open(r"data.json", "w") as file:
                #saving updated data
                json.dump(data, file, indent=4)
        finally:
                website_entry.delete(0, END)
                pass_entry.delete(0, END)








#website label

web_label = Label(text="Website:")
web_label.grid(row=1, column=0)

#website entry
website_entry = Entry(width=35)
website_entry.grid(row=1, column=0, columnspan=4)


#email label
email_label = Label(text="Email/name:")
email_label.grid(row=2, column=0)


#email and username entry
email_name_entry = Entry(width=35)
email_name_entry.grid(row=2, column=0, columnspan=4)



#passoward label
passoword_label = Label(text="Passoward:")
passoword_label.grid(row=3, column=0)


#pass entry
pass_entry = Entry(width=35)
pass_entry.grid(row=3, column=0, columnspan=3)


#generate pass button

gen_pass = Button(text="Gener", command=generate_password)
gen_pass.grid(row=3, column=2)


#add pass button
add_button = Button(text="Add", width=36, command=saving_data)
add_button.grid(row=4, column=1, columnspan=2)

#search button

search = Button(text="Search", width=10, command=search_for_data)
search.grid(row=1, column=2)





win.mainloop()
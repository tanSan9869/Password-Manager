from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# Password Generator Project
def generate_password():
    password_input.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    letter_list = [random.choice(letters) for char in range(nr_letters)]

    symbol_list = [random.choice(symbols) for char1 in range(nr_symbols)]

    number_list = [random.choice(numbers) for char2 in range(nr_numbers)]

    password_list = letter_list + symbol_list + number_list

    random.shuffle(password_list)

    password = "".join(password_list)

    # password = ""
    # for char in password_list:
    #   password += char
    password_input.insert(0, password)
    pyperclip.copy(password)

    # print(f"Your password is: {password}")
def find_password():
    website=web_input.get()
    try:
        with open("data.json","r") as data_file:
            data=json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found.")
    else:
        if website in data:
            email=data[website]["email"]
            password=data[website]["password"]
            messagebox.showinfo(title=website,message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error",message=f"No details of {website} found.")

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = web_input.get()
    email = email_input.get()
    password = password_input.get()
    new_dict = {
        website: {
            "email": email,
            "password": password
        }}

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="OOPS!", message="Please don't leave any fields empty")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json","w") as data_file:
                json.dump(new_dict,data_file,indent=4)

        else:
            data.update(new_dict)

            with open("data.json","w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            web_input.delete(0, END)
            password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Generator")
window.config(padx=20, pady=20, bg="white")

canvas = Canvas(width=300, height=300, bg="white", highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(150, 150, image=logo_img)
canvas.grid(column=1, row=0)

web_label = Label(text="Website: ", highlightthickness=0, bg="white")
web_label.grid(column=0, row=1)

web_input = Entry(width=29, bg="white")
web_input.grid(column=1, row=1, columnspan=2)
web_input.focus()

Search_button = Button(text="Search", bg="white", highlightthickness=0,width=13,command=find_password)
Search_button.grid(column=2, row=1)

email_label = Label(text="Email/Username: ", highlightthickness=0, bg="white")
email_label.grid(column=0, row=2)

email_input = Entry(width=29, bg="white")
email_input.insert(0, "tanishk@gmail.com")
email_input.grid(column=1, row=2, columnspan=2)


password_label = Label(text="Password: ", highlightthickness=0, bg="white")
password_label.grid(column=0, row=3)

password_input = Entry(width=20, bg="white")
password_input.grid(column=1, row=3)

# Button
password_generator_button = Button(text="Generate Password", bg="white", highlightthickness=0,
                                   command=generate_password)
password_generator_button.grid(column=2, row=3)

add_button = Button(text="Add", bg="white", highlightthickness=0, width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()

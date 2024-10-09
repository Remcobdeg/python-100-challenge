from tkinter import *
from tkinter import messagebox #note, since it's a module and not a class, it is not imported with the previous command
import random
import pyperclip
import json

PW_FILE = "pw_data.json"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_list += [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_list += [random.choice(numbers) for _ in range(random.randint(2, 4))]

    random.shuffle(password_list)

    password = "".join(password_list)

    p_entry.delete(0,'end')
    p_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():

    website = w_entry.get()
    user = u_entry.get()
    pw = p_entry.get()

    #store this in JSON format
    new_data = {
        website: {
            "email": user,
            "password": pw
        }
    }

    if "" in [website,user,pw]:
        messagebox.showinfo(message="Please complete all fields.", icon="warning")
    else:
        try:
            with open(PW_FILE, mode="r") as file:
                data = json.load(file) #provides a dictionary
        except FileNotFoundError:
            with open(PW_FILE, mode="w") as file:
                json.dump(new_data, file, indent=4) #indent=4 expands it for better readability
        else:
            data.update(new_data)
            with open(PW_FILE, mode="w") as file:
                json.dump(data, file, indent=4) #indent=4 expands it for better readability
        finally:
            #clear fields after save
            w_entry.delete(0,'end')
            u_entry.delete(0,'end')
            u_entry.insert(0, "default@email.com")
            p_entry.delete(0,'end')

# ---------------------------- SEARCH PASSWORD ------------------------------- #

def search_password():
    website = w_entry.get()
    try:
        with open(PW_FILE) as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(message="There are no stored passwords", icon="warning")
    else:
        try:
            found_data = data[website]
        except KeyError:
            messagebox.showinfo(message=f"{website} not found. Did you store the information under a different name? Here are the websites I've got:"
                  f"\n\n{", ".join([key for key in data])}", icon="warning")
        else:
            messagebox.showinfo(message=f"User name: {found_data["email"]}\nPassword: {found_data["password"]}", icon="warning", title=website)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(padx=20,pady=20)

canvas = Canvas(width=200, height=200)
myimg = PhotoImage(file='logo.png')
canvas.create_image(0, 0, image=myimg, anchor='nw')

canvas.grid(column=2,row=1)

#Website row
w_label = Label(text="Website:")
w_entry = Entry()
search = Button(text="Search", command=search_password, width=13)
w_label.grid(column=1,row=2)
w_entry.grid(column=2, columnspan = 2 ,row=2, sticky="W")
search.grid(column=3,row=2)
w_entry.focus()

#Username row
u_label = Label(text="Email/Username:")
u_entry = Entry(width=35)
u_entry.insert(0, "default@email.com") #index takes (mostly) 0 or END (after inserted text)
u_label.grid(column=1,row=3)
u_entry.grid(column=2, columnspan = 2 ,row=3, sticky="W")

#Password row
p_label = Label(text="Password:")
p_entry = Entry()
p_button = Button(text="Generate Password", command=generate_password)
p_label.grid(column=1,row=4)
p_entry.grid(column=2,row=4, sticky="W")
p_button.grid(column=3,row=4)

#Add button row
add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(column=2, columnspan = 2 ,row=5, sticky="W")

window.mainloop()
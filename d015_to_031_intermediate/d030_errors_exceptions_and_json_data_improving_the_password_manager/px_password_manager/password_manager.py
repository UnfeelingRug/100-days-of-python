from pyperclip import copy
from random import choice, randint, shuffle
from tkinter import *
from tkinter import messagebox
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    # Establishing the lists of letters, numbers, and symbols to pick from.
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
               'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
               'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # Pick 8-10 letters, 2-4 numbers, 2-4 symbols, add them all to a list and shuffle, then save as a string.
    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    shuffle(password_list)
    password = ''.join(password_list)

    # Copy the generated password to the clipboard, clear both password entry fields and put it there too.
    copy(password)
    inpt_password.delete(0, END)
    inpt_password.insert(END, password)
    inpt_confirm.delete(0, END)
    inpt_confirm.insert(END, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    # Fetch the info from the input boxes.
    website = inpt_website.get()
    username = inpt_user.get()
    password = inpt_password.get()
    confirm = inpt_confirm.get()

    new_data = {
        website: {
            'username': username,
            'password': password
        }
    }

    # If the user does not fill in every entry spot, or their password and confirmation do not match, inform them.
    # If neither of those cases are true, save the username and password to the data.txt file.
    if website == '' or username == '' or password == '' or confirm == '':
        messagebox.showinfo(title='Error', message='You didn\'t enter info in all three boxes.')
    elif password != confirm:
        messagebox.showinfo(title='Error', message='Your password entries do not match.')
    else:
        # Read the data file and update it with the newly entered data appended to the end.
        try:
            with open('data.json', mode='r') as f:
                data = json.load(f)
                data.update(new_data)
        # If the file doesn't exist, create it, and prepare it to accept the first piece of data.
        except FileNotFoundError:
            with open('data.json', mode='w') as f:
                data = new_data
        # If the file exists, but doesn't have any information in it, prepare it to accept the first piece of data.
        except json.decoder.JSONDecodeError:
            data = new_data
        # If neither issue comes up, write the updated data to the file, and clear the entry fields.
        finally:
            with open('data.json', mode='w') as f:
                json.dump(data, f, indent=2)

            inpt_website.delete(0, END)
            inpt_password.delete(0, END)
            inpt_confirm.delete(0, END)
            inpt_website.focus()

# ---------------------------- RETRIEVE PASSWORD ------------------------------- #
def find_password():
    # Fetches the user's input to request the website.
    website = inpt_website.get()
    if website == '':
        messagebox.showinfo(title='Error', message='You must enter a website to search.')
    else:
        # Opens the JSON file and searches for the appropriate website, giving the user feedback based on results.
        try:
            with open('data.json') as f:
                data = json.load(f)
            website_info = data[website]
        except KeyError:
            messagebox.showinfo(title='Error', message='No data exists for that website.\n'
                                                       'It has likely not been entered yet. Please do so now.')
        except json.decoder.JSONDecodeError:
            messagebox.showinfo(title='Error', message='The password database has no information in it.\n'
                                                       'Please add an account to begin filling it.')
        except FileNotFoundError:
            messagebox.showinfo(title='Error', message='The password database does not yet exist.\n'
                                                       'Please add an account to create it.')
        # If the info can be found, show it to the user. Hide the password unless the box is checked.
        else:
            username = website_info['username']
            password = website_info['password']            
            if show_pass.get() == 0:
                password = 'HIDDEN'
            messagebox.showinfo(title='Error', message=f'Username: {username}\nPassword: {password}\n\n'
                                                       f'Website password copied to clipboard.')
            copy(password)


# ---------------------------- SHOW / HIDE PASSWORD ------------------------------- #
# Enables or disables obfuscation of the password with dots when the box is toggled.
def show_hide_password():
    global show_pass
    state = show_pass.get()
    if state == 1:
        inpt_password.config(show='')
        inpt_confirm.config(show='')
    else:
        inpt_password.config(show='•')
        inpt_confirm.config(show='•')


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('UnfeelingRug\'s Password Generator')
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=0, columnspan=3)

# User input for the website the info is for.
lbl_website = Label(text='Website:')
lbl_website.grid(row=1, column=0)
inpt_website = Entry(width=25)
inpt_website.grid(row=1, column=1)
btn_password = Button(text='Search', command=find_password, width=10)
btn_password.grid(row=1, column=2)
inpt_website.focus()

# User input for the username or email address used to sign in.
lbl_user = Label(text='Email / Username:')
lbl_user.grid(row=2, column=0)
inpt_user = Entry(width=39)
inpt_user.grid(row=2, column=1, columnspan=2)
inpt_user.insert(END, 'fake-address@test.email')

# User input for the password used to sign in, and the confirmation.
# Included is a button to generate a password, and a checkbox to toggle showing or hiding them.
lbl_password = Label(text='Password:')
lbl_password.grid(row=3, column=0)
inpt_password = Entry(width=25, show='•')
inpt_password.grid(row=3, column=1)
btn_password = Button(text='Generate', command=generate_password, width=10)
btn_password.grid(row=3, column=2)

lbl_confirm = Label(text='Confirm Password:')
lbl_confirm.grid(row=4, column=0)
inpt_confirm = Entry(width=25, show="•")
inpt_confirm.grid(row=4, column=1)
show_pass = IntVar()
show_password = Checkbutton(text='Show', variable=show_pass, onvalue=1, offvalue=0, command=show_hide_password, width=10)
show_password.grid(row=4, column=2)

# Button to add all of the supplied data to the data.txt file, saving the information.
btn_add = Button(text='Add', command=add_password, width=32)
btn_add.grid(row=5, column=1, columnspan=2)

window.mainloop()

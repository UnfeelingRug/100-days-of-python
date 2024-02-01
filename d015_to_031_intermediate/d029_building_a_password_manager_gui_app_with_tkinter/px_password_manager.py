from pyperclip import copy
from random import choice, randint, shuffle
from tkinter import *
from tkinter import messagebox

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

    # If the user does not fill in every entry spot, or their password and confirmation do not match, inform them.
    # If neither of those cases are true, save the username and password to the data.txt file.
    if website == '' or username == '' or password == '' or confirm == '':
        messagebox.showinfo(title='Error', message='You didn\'t enter info in all three boxes.')
    elif password != confirm:
        messagebox.showinfo(title='Error', message='Your password entries do not match.')
    else:
        # Debug option; message box to confirm username and password to save. If uncommenting this, indent the rest of the function.
        # is_ok = messagebox.askokcancel(title=website, message=f'These are the details entered:\nEmail: {username}\nPassword: {password}\nIs that okay to save?')
        # if is_ok:
        with open('data.txt', mode='a') as f:
            f.write(('\n' + website + ' | ' + username + ' | ' + password))

        inpt_website.delete(0, END)
        inpt_password.delete(0, END)
        inpt_website.focus()

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
inpt_website = Entry(width=39)
inpt_website.grid(row=1, column=1, columnspan=2)
inpt_website.focus()

# User input for the username or email address used to sign in.
lbl_user = Label(text='Email / Username:')
lbl_user.grid(row=2, column=0)
inpt_user = Entry(width=39)
inpt_user.grid(row=2, column=1, columnspan=2)
inpt_user.insert(END, 'fake-address@test.email')

# User input for the password used to sign in, and the confirmation. Included is a button to generate a password.
lbl_password = Label(text='Password:')
lbl_password.grid(row=3, column=0)
inpt_password = Entry(width=20, show='•')
inpt_password.grid(row=3, column=1)
btn_password = Button(text='Generate Password', command=generate_password, width=15)
btn_password.grid(row=3, column=2)

lbl_confirm = Label(text='Confirm Password:')
lbl_confirm.grid(row=4, column=0)
inpt_confirm = Entry(width=39, show="•")
inpt_confirm.grid(row=4, column=1, columnspan=2)

# Button to add all of the supplied data to the data.txt file, saving the information.
btn_add = Button(text='Add', command=add_password, width=32)
btn_add.grid(row=5, column=1, columnspan=2)

window.mainloop()

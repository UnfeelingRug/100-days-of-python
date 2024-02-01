from tkinter import *


# When the established button is clicked, edit the Label to display the text retrieved from the entry field.
def button_clicked():
    my_label.config(text=user_input.get())


# Get the current number of the spinbox below and insert it into the title.
def spinbox_used():
    window.title('UnfeelingRug\'s First GUI Program - #' + str(spinbox.get()))


# Create a window
window = Tk()
window.title('UnfeelingRug\'s First GUI Program')
window.minsize(width=500, height=300)

# Create a label.
my_label = Label(text='This is Damien\'s first label.', font=('Comfortaa', 18, 'bold'))
my_label.pack()

# Create an entry field, to accept user input.
user_input = Entry(width=25)
user_input.pack()

# Create a button.
button = Button(text='Change the label!', command=button_clicked)
button.pack()

# Create a text field.
text = Text(height=5, width=30)
text.focus()
text.pack()

# Create a spinbox.
spinbox = Spinbox(from_=0, to=10, width=2, command=spinbox_used)
spinbox.pack()

# Create a scale.
scale = Scale(from_=0, to=100)
scale.pack()

# Create a checkbox.
checked_state = IntVar()
checkbox = Checkbutton(text='Is On?', variable=checked_state)
checkbox.pack()

# Create a series of radio buttons.
radio_state = IntVar()
radio_button_1 = Radiobutton(text='Option 1', value=1, variable=radio_state)
radio_button_2 = Radiobutton(text='Option 2', value=2, variable=radio_state)
radio_button_1.pack()
radio_button_2.pack()

# Create a listbox.
fruits = ['Apple', 'Banana', 'Orange', 'Pear']
listbox = Listbox(height=4)
for i in fruits:
    listbox.insert(fruits.index(i), i)
listbox.pack()

window.mainloop()

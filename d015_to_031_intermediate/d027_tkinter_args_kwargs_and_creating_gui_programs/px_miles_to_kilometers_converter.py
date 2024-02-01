from tkinter import *


# When the button is clicked, calculate the miles to kilometers conversion and print it to the label.
def button_clicked():
    result = round(int(user_input.get()) * 1.60934, 2)
    result_label.config(text=result)


# Create a window
window = Tk()
window.title('Miles to Kilometers Converter')
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)

# Row One - "## Miles"
user_input = Entry(width=5)
user_input.grid(row=0, column=1)

miles_label = Label(text='miles', font=('Times New Roman', 12, 'normal'))
miles_label.grid(row=0, column=2)

# Row Two - "is equal to ## km"
equal_to_label = Label(text='is equal to', font=('Times New Roman', 12, 'normal'))
equal_to_label.grid(row=1, column=0)

result_label = Label(text='', font=('Times New Roman', 12, 'normal'))
result_label.grid(row=1, column=1)

km_label = Label(text='kilometers', font=('Times New Roman', 12, 'normal'))
km_label.grid(row=1, column=2)

# Button to run the calculation.
calculate_btn = Button(text='Calculate', command=button_clicked)
calculate_btn.grid(row=2, column=1)

window.mainloop()

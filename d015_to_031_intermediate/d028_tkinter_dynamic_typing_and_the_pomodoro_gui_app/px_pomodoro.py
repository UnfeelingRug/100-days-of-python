# ---------------------------- IMPORTS ------------------------------- #
from math import floor
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
RED = '#e7305b'
YELLOW = '#f7f5dd'
FONT_NAME = 'Comfortaa'
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps, timer
    window.after_cancel(timer)
    reps = 0
    lbl_title.config(text='Pomodoro')
    lbl_progress.config(text='')
    canvas.itemconfig(timer_text, text='00:00')


# ---------------------------- TIMER MECHANISM ------------------------------- # 
# Begin the timer, setting the length and label based on the current stage (work, short break, long break)
# When reaching a new break, increase the number of check marks.
def start_timer():
    global reps
    if reps % 2 == 0:
        count_down(WORK_MIN * 60)
        lbl_title.config(text='Work')
        reps += 1
    elif reps % 7 == 0:
        count_down(LONG_BREAK_MIN * 60)
        lbl_title.config(text='Break')
        reps += 1
    else:
        count_down(SHORT_BREAK_MIN * 60)
        lbl_title.config(text='Break')
        reps += 1
    lbl_progress.config(text='🗸' * int(reps / 2))

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
# Define the number of minutes and seconds, then print it to the timer and count down.
# When the timer hits zero, begin the timer again to progress to the next break or work period.
def count_down(count):
    minutes = floor(count/60)
    seconds = str(count % 60).zfill(2)
    count_formatted = f'{minutes}:{seconds}'
    canvas.itemconfig(timer_text, text=count_formatted)
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
# Create the window, with the title background colour, and padding.
window = Tk()
window.title('UnfeelingRug\'s Pomodoro App')
window.config(padx=100, pady=20, bg=YELLOW)

# Add the big label at the top.
lbl_title = Label(text='Pomodoro', font=(FONT_NAME, 25, 'bold'), fg=RED, bg=YELLOW)
lbl_title.grid(row=0, column=1)

# Add the Pomodoro timer, with the tomato and timer.
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text='00:00', font=(FONT_NAME, 18, 'bold'), fill='white')
canvas.grid(row=1, column=1, pady=(5, 30))

# Add the Start and Reset buttons, as well as their functionality.
btn_start = Button(text='Start', width=6, command=start_timer)
btn_start.grid(row=2, column=0)
btn_reset = Button(text='Reset', width=6, command=reset_timer)
btn_reset.grid(row=2, column=2)

# Add the label to show the progress through Pomodoros as check marks.
lbl_progress = Label(font=(FONT_NAME, 20, 'bold'), fg=RED, bg=YELLOW)
lbl_progress.grid(row=3, column=1)

window.mainloop()

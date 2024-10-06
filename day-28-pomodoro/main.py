from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global reps

    window.after_cancel(timer)
    reps = 0
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    checkmark.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1

    if reps%8 == 0:
        count = LONG_BREAK_MIN *60
        title_label.config(text="Break", fg=RED)
    elif reps%2 == 0:
        count = SHORT_BREAK_MIN *60
        title_label.config(text="Break", fg=PINK)
    else:
        count = WORK_MIN *60
        title_label.config(text="Work", fg=GREEN)

    count_down(count)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):

    global timer #we needed to make the window.after() a named variable that global so we can access it to cancel it later

    count_min = math.floor(count/60)
    count_sec = count%60
    if count_sec <10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count>0:
        timer = window.after(1000, count_down, count-1) #async function executing after set time -- note that a function can call itself :)
    else:
        checks = "✓"*math.floor(reps/2)
        checkmark.config(text=checks)
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

#title label
title_label = Label(text="Timer", font=(FONT_NAME,40), fg=GREEN, bg=YELLOW)
title_label.grid(column=2,row=1)

#canvas widget (tomato + timer)
canvas = Canvas(width=200,height=224,bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112, image=tomato_img) #x and y positions (here approximately centered on screen
timer_text = canvas.create_text(100,130, text="00:00", fill = "white", font=(FONT_NAME,35,"bold")) #by giving it a name we can call it elsewhere
canvas.grid(column=2,row=2)

#start button
start_button = Button(text="Start", highlightbackground=YELLOW, command=start_timer)
start_button.grid(column=1,row=3)

#reset button
reset_button = Button(text="Reset", highlightbackground=YELLOW, command=reset)
reset_button.grid(column=3,row=3)

#checkmark
checkmark = Label(bg=YELLOW, fg=GREEN)
checkmark.grid(column=2,row=4)

window.mainloop()







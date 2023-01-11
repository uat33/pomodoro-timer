from tkinter import *
import math
from playsound import playsound

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
ALARM = "alarm.wav"
CHECKMARK = "✓"

class timer_UI:
    
    def __init__(self):
        self.reps = 0
        self.timer = None
        
        self.window = Tk()
        tomato_img = PhotoImage(file="tomato.png")
        self.window.title("Pomodoro Timer")
        self.window.config(padx=100, pady=50, bg=YELLOW)
        self.canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
        self.canvas.create_image(100, 112, image=tomato_img)
        self.canvas.grid(row=1, column=1)
        self.timer_text = self.canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

        # timer label

        self.timer_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 35, "bold"), bg=YELLOW)
        self.timer_label.grid(column=1, row=0)

        # start button

        self.start_button = Button(text="Start", command=self.start_timer, bg=YELLOW, highlightbackground=YELLOW)
        self.start_button.grid(column=0, row=2)

        # reset button

        self.reset_button = Button(text="Reset", command=self.reset_timer, highlightbackground=YELLOW)
        self.reset_button.grid(column=3, row=2)

        # checkmark

        self.checkmark = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, "bold"))
        self.checkmark.grid(row=3, column=1)

        self.window.mainloop()

    def reset_timer(self):
        self.window.after_cancel(self.timer)
        self.canvas.itemconfig(self.timer_text, text='00:00')
        self.timer_label.config(text="Timer")
        self.checkmark.config(text="")
        self.reps = 0

    def start_timer(self):
        self.reps += 1

        if self.reps % 2 != 0:
            self.countdown(WORK_MIN * 60)
            self.timer_label.config(text="WORK", fg=GREEN)
        elif self.reps % 8 == 0:
            self.countdown(LONG_BREAK_MIN * 60)
            self.timer_label.config(text="BREAK", fg=RED)
        else:
            self.countdown(SHORT_BREAK_MIN * 60)
            self.timer_label.config(text="BREAK", fg=PINK)


    def countdown(self, count):
        minute = math.floor(count / 60)
        sec = count % 60

        if sec < 10:
            sec = f"0{sec}"

        self.canvas.itemconfig(self.timer_text, text=f"{minute}:{sec}")
        if count > 0:
            # after -- executes command after time delay
            self.timer = self.window.after(1000, self.countdown, count - 1)
        else:
            playsound(ALARM)
            self.start_timer()
            if self.reps % 2 == 0:
                self.checkmark.config(text=self.checkmark['text'] + CHECKMARK)


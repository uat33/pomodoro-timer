from tkinter import *
import math
from playsound import playsound


# constants
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 25
ALARM = "alarm.wav"
TALLY = "/"

class timer_UI:
    
    def __init__(self):
        # reps are the total number of sessions
        # use this to keep track of how long the current session should be
        # initialize to 0
        self.reps = 0 
        # initalize timer to None
        self.timer = None
        
        self.window = Tk() # create the window
        # tomato_img = PhotoImage(file="tomato.png") # create the image
        self.window.title("Pomodoro Timer") # title our window
        self.window.config(padx=100, pady=50, bg=YELLOW) # format our window
        self.canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0) # create and format our canvas
        # self.canvas.create_image(100, 112, image=tomato_img) # add image to canvas
        self.canvas.grid(row=1, column=1) # add canvas to window
        # make the timer itself on the canvas
        self.timer_text = self.canvas.create_text(100, 130, text="00:00", fill="black", font=(FONT_NAME, 35, "bold"))

        # timer label
        self.timer_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 35, "bold"), bg=YELLOW)
        self.timer_label.grid(column=1, row=0) # add timer label to window

        # start button
        # create the button for starting timer
        self.start_button = Button(text="Start", command=self.start_timer, bg=YELLOW, highlightbackground=YELLOW)
        self.start_button.grid(column=0, row=2) # add it to window

        # reset button

        self.reset_button = Button(text="Reset", command=self.reset_timer, highlightbackground=YELLOW)
        self.reset_button.grid(column=3, row=2) # add it to window

        # tally
        # shows the total number of work sessions completed
        # create a label 
        self.tally = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, "bold"))
        self.tally.grid(row=3, column=1) # add it 
        # it starts off as empty

        self.window.mainloop() # the mainloop

    # the starting screen
    def reset_timer(self):

        # resets the timer so we don't have to exit to restart
        self.window.after_cancel(self.timer) 

        # reset text, and label and tallies
        self.canvas.itemconfig(self.timer_text, text='00:00')
        self.timer_label.config(text="Timer")
        self.tally.config(text="")

        # make the start button normal so it can be restarted
        self.start_button.config(state=NORMAL)
        # set sessions to 0
        self.reps = 0

    def start_timer(self):
        self.reps += 1 # add one to the sessions count

        if self.reps % 2 != 0: # if it is a work session
            self.countdown(WORK_MIN * 60) # calculate seconds
            self.timer_label.config(text="WORK", fg=GREEN) # add appropriate label
        elif self.reps % 8 == 0: # it's a long break
            self.countdown(LONG_BREAK_MIN * 60) # calculate seconds
            self.timer_label.config(text="BREAK", fg=RED) # add appropriate label
        else: # it must be a short break
            self.countdown(SHORT_BREAK_MIN * 60) # calculate seconds
            self.timer_label.config(text="BREAK", fg=PINK) # add appropriate label
        self.start_button.config(state=DISABLED) # disable the starting button, cause we don't want to start multiple timers

    def countdown(self, count):
        minute = math.floor(count / 60) # calculate the minutes
        sec = count % 60 # and seconds

        if sec < 10: # add 0 in front of seconds if needed
            sec = f"0{sec}"

        self.canvas.itemconfig(self.timer_text, text=f"{minute}:{sec}") # update the timer
        if count > 0: # call this function every second when the timer is counting down
            # after -- executes command after time delay
            self.timer = self.window.after(1000, self.countdown, count - 1)
        else: # when timer hits 0
            # play an alarm
            playsound(ALARM)
            # when that's done, start the itmer again
            self.start_timer()
            if self.reps % 2 == 0: # if it was a work session
                # add a tally
                self.tally.config(text=self.tally['text'] + TALLY)


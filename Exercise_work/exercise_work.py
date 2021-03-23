# File:         Ex8_5
# Author:       Niki Leppänen
# Description:  Simple GUI with tkinter, main screen has buttons that opens different applications/games
#               (alarm clock, card games, dice roll, ect.)

import datetime
import winsound
import tkinter.messagebox
from time import strftime
from tkinter import *
from tkinter.ttk import *

from Exercise_work.paint_app import paint
from Exercise_work.alarm_clock import AlarmClock
from Exercise_work.player import Player



root = Tk()
root.geometry('200x400')


def money_amount():
    player = Player()
    money = player
    money_lbl.config(text=money)


# function for getting current time
def current_time():
    time = strftime('%H:%M:%S')
    time_lbl.config(text=time)
    time_lbl.after(1000, current_time)


def alarm_clock_app():
    alarm = AlarmClock()

    alarm_window = Toplevel(root)

    def alarm_ring(set_alarm_timer):
        while True:
            current = datetime.datetime.now()
            now = current.strftime("%H:%M:%S")
            if now == set_alarm_timer:
                winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
                tkinter.messagebox.showinfo(title="Alarm!!!", message="Wake up!!!")
                break

    def alarm_set():
        alarm_time = "%s:%s:00" % (hours.get(), mins.get())

        alarm.set_alarm(alarm_time)
        print(alarm.get_alarm_time())
        print(alarm.get_time())

        alarm_ring(alarm.get_alarm_time())

    alarm_window.title("Alarm clock")

    alarm_window.geometry("250x100")

    hour_lbl = Label(alarm_window, font=('calibri', 14, 'bold'), text="HOURS")
    mins_lbl = Label(alarm_window, font=('calibri', 14, 'bold'), text="MINS")
    hour_lbl.place(y=8, x=54)
    mins_lbl.place(y=8, x=136)

    hours = Entry(alarm_window, width=9)
    mins = Entry(alarm_window, width=9)

    hours.place(y=30, x=56)
    mins.place(y=30, x=136)

    set_alarm = Button(alarm_window, text="Set alarm", command=alarm_set)
    set_alarm.place(y=60, x=88)


def poker_game():
    poker = Toplevel(root)
    poker.title("Poker")
    poker.geometry('1200x800')
    poker.configure(bg='green')


def dice_game():
    dice = Toplevel(root)
    dice.title("Dice game")
    dice.geometry('800x800')
    dice.configure(bg='blue')


# Text area for clock
time_lbl = Label(root, font=('calibri', 10, 'bold'))
time_lbl.pack(anchor='ne')
current_time()

money_lbl = Label(root, font=('calibri', 10, 'bold'))
money_lbl.pack(anchor='nw')
money_amount()

# logos for buttons
paint_logo = PhotoImage(file=r"C:\Users\Niki\Desktop\Olio-ohjelmointi\Images\paint.png")

# buttons for apps
paint_btn = Button(root, text="PAINT", command=paint)
paint_btn.pack(pady=10)

alarm_btn = Button(root, text="Alarm clock", command=alarm_clock_app)
alarm_btn.pack(pady=10)

poker_btn = Button(root, text="Poker", command=poker_game)
poker_btn.pack(pady=10)

dice_btn = Button(root, text="Dice game", command=dice_game)
dice_btn.pack(pady=10)


mainloop()

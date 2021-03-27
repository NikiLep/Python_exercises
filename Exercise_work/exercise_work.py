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
from PIL import ImageTk,Image

from Exercise_work.paint_app import paint
from Exercise_work.alarm_clock import AlarmClock
from Exercise_work.player import Player
from Exercise_work.dice import Dice


root = Tk()
root.geometry('200x400')


def money_amount():
    money = player
    money_lbl.config(text=money)
    money_lbl.after(1000, money_amount)


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
    def game_bet():
        bet_size = int("%s" % (bet.get()))
        return bet_size

    def game():

        computer1.roll_dice()
        computer2.roll_dice()
        player1.roll_dice()
        player2.roll_dice()

        computer_total = computer1.get_dice() + computer2.get_dice()
        player_total = player1.get_dice() + player2.get_dice()

        if computer_total > player_total:
            player.set_money(player.get_money()-game_bet())
            lose_lbl.place(x=355, y=260)
            print(player)

        elif player_total > computer_total:
            player.set_money(player.get_money()+game_bet())
            win_lbl.place(x=355, y=260)
            print(player)

        else:
            tie_lbl.place(x=355, y=260)
            print(player)

        # show rolled dices
        print(player1.get_dice())
        print(player2.get_dice())
        print(computer1.get_dice())
        print(computer2.get_dice())

        computer_dice1 = Label(dice, image=dices[computer1.get_dice() - 1])
        computer_dice2 = Label(dice, image=dices[computer2.get_dice() - 1])
        player_dice1 = Label(dice, image=dices[player1.get_dice() - 1])
        player_dice2 = Label(dice, image=dices[player2.get_dice() - 1])

        computer_dice1.place(x=230, y=80)
        computer_dice2.place(x=430, y=80)
        player_dice1.place(x=230, y=350)
        player_dice2.place(x=430, y=350)

    # objects for dice game
    computer1 = Dice()
    computer2 = Dice()
    player1 = Dice()
    player2 = Dice()

    # configures for the dice window
    dice = Toplevel(root)
    dice.title("Dice game")
    dice.geometry('800x600')

    # dice window text label on top of the screen
    top_lbl = Label(dice, text="Roll higher than computer", font=('calibri', 20, 'bold'))
    top_lbl.pack(anchor='n')

    # pictures of all the dices
    dice1 = ImageTk.PhotoImage(Image.open("C:/Users/Niki/Desktop/Olio-ohjelmointi/Images/dice1.png"))
    dice2 = ImageTk.PhotoImage(Image.open("C:/Users/Niki/Desktop/Olio-ohjelmointi/Images/dice2.png"))
    dice3 = ImageTk.PhotoImage(Image.open("C:/Users/Niki/Desktop/Olio-ohjelmointi/Images/dice3.png"))
    dice4 = ImageTk.PhotoImage(Image.open("C:/Users/Niki/Desktop/Olio-ohjelmointi/Images/dice4.png"))
    dice5 = ImageTk.PhotoImage(Image.open("C:/Users/Niki/Desktop/Olio-ohjelmointi/Images/dice5.png"))
    dice6 = ImageTk.PhotoImage(Image.open("C:/Users/Niki/Desktop/Olio-ohjelmointi/Images/dice6.png"))

    dices = (dice1, dice2, dice3, dice4, dice5, dice6)

    bet = Entry(dice, width=12)
    bet.place(x=700, y=300)

    bet_lbl = Label(dice, text="Your bet", font=('calibri', 16, 'bold'))
    bet_lbl.place(x=698, y=270)

    roll_btn = Button(dice, text="ROLL", command=game)
    roll_btn.place(x=365, y=500)

    # Win/Lose/Tie labels
    win_lbl = Label(dice, text="You won", font=('calibri', 20, 'bold'))
    lose_lbl = Label(dice, text="You lost", font=('calibri', 20, 'bold'))
    tie_lbl = Label(dice, text="Tie", font=('calibri', 20, 'bold'))

    win_lbl.config(foreground='red')
    lose_lbl.config(foreground='red')
    tie_lbl.config(foreground='red')



# Text area for clock
time_lbl = Label(root, font=('calibri', 10, 'bold'))
time_lbl.pack(anchor='ne')
current_time()

# keeps track on players money
player = Player()

money_lbl = Label(root, font=('calibri', 10, 'bold'))
money_lbl.place(x=0, y=0)
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

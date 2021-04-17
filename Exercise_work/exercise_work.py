# File:         exercise_work
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
from Exercise_work.deck import Deck
from Exercise_work.cards import Card

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

    # function for checking if alarm time is equal to current time and then sets of alarm
    def alarm_ring(set_alarm_timer):
        while True:
            current = datetime.datetime.now()
            now = current.strftime("%H:%M:%S")
            if now == set_alarm_timer:
                winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
                tkinter.messagebox.showinfo(title="Alarm!!!", message="Wake up!!!")
                break

    # function to get alarm time from entry box
    def alarm_set():
        alarm_time = "%s:%s:00" % (hours.get(), mins.get())

        alarm.set_alarm(alarm_time)
        print(alarm.get_alarm_time())
        print(alarm.get_time())

        alarm_ring(alarm.get_alarm_time())

    alarm_window.title("Alarm clock")

    alarm_window.geometry("250x100")

    # all the texts on the window
    hour_lbl = Label(alarm_window, font=('calibri', 14, 'bold'), text="HOURS")
    mins_lbl = Label(alarm_window, font=('calibri', 14, 'bold'), text="MINS")
    hour_lbl.place(y=8, x=54)
    mins_lbl.place(y=8, x=136)

    # entry widgets
    hours = Entry(alarm_window, width=9)
    mins = Entry(alarm_window, width=9)

    hours.place(y=30, x=56)
    mins.place(y=30, x=136)

    # Buttons
    set_alarm = Button(alarm_window, text="Set alarm", command=alarm_set)
    set_alarm.place(y=60, x=88)


def poker_game():
    # sorting function
    def highest(list):
        for step in range(1, len(list)):
            key = list[step]
            j = step - 1

            while j >= 0 and key.get_value() > list[j].get_value():
                list[j + 1] = list[j]
                j = j - 1

            list[j + 1] = key

    # finds player with best hand/score
    def winner(list):
        for step in range(1, len(list)):
            key = list[step]
            j = step - 1

            while j >= 0 and key.get_score() > list[j].get_score():
                list[j + 1] = list[j]
                j = j - 1

            list[j + 1] = key

    # Scoring of hands:
    # Straight flush = 120 - 134
    # Four of a kind = 105 - 119
    # Full house = 90 - 104
    # Flush = 75 - 89
    # Straight = 60 - 74
    # Three of a kind = 45 - 59
    # Two pair = 30 - 44
    # Pair = 15 - 29
    # High Card = 2 - 14

    # Checks for pair
    def check_pair(hand):
        # puts cards in order from highest to lowest value
        highest(hand)

        if len(hand) < 2:
            return 0
        elif hand[0].get_value() == hand[1].get_value():
            score = 15 + hand[0].get_value()

            return score
        else:
            return check_pair(hand[1:])

    # Checks for three of a kind
    def check_triple(hand):
        # puts cards in order from highest to lowest value
        highest(hand)

        if len(hand) < 3:
            return 0
        elif hand[0].get_value() == hand[1].get_value() == hand[2].get_value():
            score = 45 + hand[0].get_value()

            return score
        else:
            return check_triple(hand[1:])

    # Checks for fours of a kind
    def check_four(hand):
        # puts cards in order from highest to lowest value
        highest(hand)

        if len(hand) < 4:
            return 0
        elif hand[0].get_value() == hand[1].get_value() == hand[2].get_value() == hand[3].get_value():
            score = 105 + hand[0].get_value()

            return score
        else:
            return check_four(hand[1:])

    # Checks for two pairs
    def check_two_pairs(hand):
        # puts cards in order from highest to lowest value
        highest(hand)
        pairs = []

        # adds pairs to pairs list
        if hand[0].get_value() == hand[1].get_value() and hand[2].get_value() == hand[3].get_value():
            pairs.append(hand[0].get_value())
            pairs.append(hand[1].get_value())
            pairs.append(hand[2].get_value())
            pairs.append(hand[3].get_value())

        elif hand[0].get_value() == hand[1].get_value() and hand[3].get_value() == hand[4].get_value():
            pairs.append(hand[0].get_value())
            pairs.append(hand[1].get_value())
            pairs.append(hand[3].get_value())
            pairs.append(hand[4].get_value())

        elif hand[1].get_value() == hand[2].get_value() and hand[3].get_value() == hand[4].get_value():
            pairs.append(hand[1].get_value())
            pairs.append(hand[2].get_value())
            pairs.append(hand[3].get_value())
            pairs.append(hand[4].get_value())

        # checks if there is two pairs in pairs list and gives score depending on both pair values
        if len(pairs) == 4:
            score = 0
            for i in pairs:
                score += i

            score = score / 4 + 30

            return score

        else:
            return 0

    # Checks for straight
    def check_straight(hand):
        # puts cards in order from highest to lowest value
        highest(hand)

        if (hand[0].get_value() - 1 == hand[1].get_value() and hand[1].get_value() - 1 == hand[2].get_value() and
                hand[2].get_value() - 1 == hand[3].get_value() and hand[3].get_value() - 1 == hand[4].get_value()):

            score = 60 + hand[0].get_value()

            return score

        else:
            return 0

    # checks for flush
    def check_flush(hand):
        # puts cards in order from highest to lowest value
        highest(hand)

        if (hand[0].get_suit() == hand[1].get_suit() and hand[1].get_suit() == hand[2].get_suit() and
                hand[2].get_suit() == hand[3].get_suit() and hand[3].get_suit() == hand[4].get_suit()):

            score = 75 + hand[0].get_value()

            return score

        else:
            return 0

    # Checks for straight flush
    def check_straight_flush(hand):

        if check_flush(hand) > 75 and check_straight(hand) > 60:
            # puts cards in order from highest to lowest value
            highest(hand)

            score = 120 + hand[0].get_value()

            return score

        else:
            return 0

    # Checks for full house
    def check_full_house(hand):
        # puts cards in order from highest to lowest value
        highest(hand)

        score = 0

        # checks for possible ways to get full house with five cards
        if (hand[0].get_value() == hand[1].get_value()
                and hand[2].get_value() == hand[3].get_value() == hand[4].get_value()):

            for i in hand:
                score += i.get_value()

            score /= 5
            score += 90

        elif (hand[0].get_value() == hand[1].get_value() == hand[2].get_value()
              and hand[3].get_value() == hand[4].get_value()):

            for i in hand:
                score += i.get_value()

            score /= 5
            score += 90

        else:
            return 0

    # function to check what is the best possible hand that player can get from his five cards and returns the score
    def check_best_hand(hand):

        score = 0

        if check_straight_flush(hand) != 0:
            score = check_straight_flush(hand)

        elif check_four(hand) != 0 and score == 0:
            score = check_four(hand)

        elif check_full_house(hand) != 0 and score == 0:
            score = check_full_house(hand)

        elif check_flush(hand) != 0 and score == 0:
            score = check_flush(hand)

        elif check_straight(hand) != 0 and score == 0:
            score = check_straight(hand)

        elif check_triple(hand) != 0 and score == 0:
            score = check_triple(hand)

        elif check_two_pairs(hand) != 0 and score == 0:
            score = check_two_pairs(hand)

        elif check_pair(hand) != 0 and score == 0:
            score = check_pair(hand)

        else:
            highest(hand)
            score = hand[0].get_value()

        print()
        print(score)

        return score

    # Shuffle deck and give cards
    def create_game():

        # shuffles the deck
        deck.shuffle_deck()

        # Gives everyone 5 cards at the beginning
        for n in range(5):
            for i in players_cards:
                i.append(deck.draw_card())

        print()

        # prints player name and his cards
        for i in players_cards:
            print()
            pos = players_cards.index(i)
            print(players[pos].get_name(), ":")
            for c in i:
                c.show_card()

        def show_card(card):
            suit = []
            if card.get_suit() == "Clubs":
                suit = clubs
            elif card.get_suit() == "Spades":
                suit = spades
            elif card.get_suit() == "Diamonds":
                suit = diamonds
            elif card.get_suit() == "Hearts":
                suit = hearts

            return suit[card.get_value()-2]



    def check_winner():
        # checks every players best hand and gives them score from it
        computer1.set_score(check_best_hand(comp_c1))
        computer2.set_score(check_best_hand(comp_c2))
        computer3.set_score(check_best_hand(comp_c3))
        player.set_score(check_best_hand(player_c))

        # tells who is the winner
        winner(players)

        print("Winner is ", players[0].get_name())

    def money_amount_p():
        money = player
        money_lbl_p.config(text=money)
        money_lbl_p.after(1000, money_amount)

    def game_bet():
        bet_size = int("%s" % (poker_bet.get()))
        return bet_size

    poker = Toplevel(root)
    poker.title("Poker")

    # creates empty canvas and stretches it to fit on the window
    canvas = Canvas(poker, background='green', width=1200, height=800)
    canvas.create_line(0, 600, 1200, 600, fill='black')
    canvas.create_line(200, 0, 200, 800, fill='black')
    canvas.pack()

    money_lbl_p = Label(poker, font=('calibri', 16, 'bold'), background='green')
    money_lbl_p.place(x=2, y=616)
    money_amount_p()

    poker_bet = Entry(poker, width=12)
    poker_bet.place(x=5, y=690)

    bet_lbl = Label(poker, text="Bet amount", font=('calibri', 14, 'bold'), background='green')
    bet_lbl.place(x=3, y=660)

    poker_button = Button(poker, text="Play", command=create_game, width=30)
    poker_button.place(x=5, y=775)

    switch_button = Button(poker, text='Switch')

    check1 = Checkbutton(poker, onvalue=1, offvalue=0)
    check2 = Checkbutton(poker, onvalue=1, offvalue=0)
    check3 = Checkbutton(poker, onvalue=1, offvalue=0)
    check4 = Checkbutton(poker, onvalue=1, offvalue=0)
    check5 = Checkbutton(poker, onvalue=1, offvalue=0)

    # all the pics of cards
    # Spades
    s2 = ImageTk.PhotoImage(Image.open("C:/Users/Niki/Desktop/Olio-ohjelmointi/Images/cards/2-s.png"))
    s3 = ImageTk.PhotoImage(Image.open("C:/Users/Niki/Desktop/Olio-ohjelmointi/Images/cards/3-s.png"))
    s4 = ImageTk.PhotoImage(Image.open("C:/Users/Niki/Desktop/Olio-ohjelmointi/Images/cards/4-s.png"))
    s5 = ImageTk.PhotoImage(Image.open("C:/Users/Niki/Desktop/Olio-ohjelmointi/Images/cards/5-s.png"))
    s6 = ImageTk.PhotoImage(Image.open("C:/Users/Niki/Desktop/Olio-ohjelmointi/Images/cards/6-s.png"))
    s7 = ImageTk.PhotoImage(Image.open("C:/Users/Niki/Desktop/Olio-ohjelmointi/Images/cards/7-s.png"))
    s8 = ImageTk.PhotoImage(Image.open("C:/Users/Niki/Desktop/Olio-ohjelmointi/Images/cards/8-s.png"))
    s9 = ImageTk.PhotoImage(Image.open("C:/Users/Niki/Desktop/Olio-ohjelmointi/Images/cards/9-s.png"))
    s10 = ImageTk.PhotoImage(Image.open("C:/Users/Niki/Desktop/Olio-ohjelmointi/Images/cards/10-s.png"))
    s11 = ImageTk.PhotoImage(Image.open("C:/Users/Niki/Desktop/Olio-ohjelmointi/Images/cards/J-s.png"))
    s12 = ImageTk.PhotoImage(Image.open("C:/Users/Niki/Desktop/Olio-ohjelmointi/Images/cards/Q-s.png"))
    s13 = ImageTk.PhotoImage(Image.open("C:/Users/Niki/Desktop/Olio-ohjelmointi/Images/cards/K-s.png"))
    s14 = ImageTk.PhotoImage(Image.open("C:/Users/Niki/Desktop/Olio-ohjelmointi/Images/cards/A-s.png"))
    # Clubs
    c2 = ImageTk.PhotoImage(Image.open("C:/Users/Niki/Desktop/Olio-ohjelmointi/Images/cards/2-c.png"))
    c3 = ImageTk.PhotoImage(Image.open("C:/Users/Niki/Desktop/Olio-ohjelmointi/Images/cards/3-c.png"))
    c4 = ImageTk.PhotoImage(Image.open("C:/Users/Niki/Desktop/Olio-ohjelmointi/Images/cards/4-c.png"))
    c5 = ImageTk.PhotoImage(Image.open("C:/Users/Niki/Desktop/Olio-ohjelmointi/Images/cards/5-c.png"))
    c6 = ImageTk.PhotoImage(Image.open("C:/Users/Niki/Desktop/Olio-ohjelmointi/Images/cards/6-c.png"))
    c7 = ImageTk.PhotoImage(Image.open("C:/Users/Niki/Desktop/Olio-ohjelmointi/Images/cards/7-c.png"))
    c8 = ImageTk.PhotoImage(Image.open("C:/Users/Niki/Desktop/Olio-ohjelmointi/Images/cards/8-c.png"))
    c9 = ImageTk.PhotoImage(Image.open("C:/Users/Niki/Desktop/Olio-ohjelmointi/Images/cards/9-c.png"))
    c10 = ImageTk.PhotoImage(Image.open("C:/Users/Niki/Desktop/Olio-ohjelmointi/Images/cards/10-c.png"))
    c11 = ImageTk.PhotoImage(Image.open("C:/Users/Niki/Desktop/Olio-ohjelmointi/Images/cards/J-c.png"))
    c12 = ImageTk.PhotoImage(Image.open("C:/Users/Niki/Desktop/Olio-ohjelmointi/Images/cards/Q-c.png"))
    c13 = ImageTk.PhotoImage(Image.open("C:/Users/Niki/Desktop/Olio-ohjelmointi/Images/cards/K-c.png"))
    c14 = ImageTk.PhotoImage(Image.open("C:/Users/Niki/Desktop/Olio-ohjelmointi/Images/cards/A-c.png"))
    # Diamonds
    d2 = ImageTk.PhotoImage(Image.open("C:/Users/Niki/Desktop/Olio-ohjelmointi/Images/cards/2-d.png"))
    d3 = ImageTk.PhotoImage(Image.open("C:/Users/Niki/Desktop/Olio-ohjelmointi/Images/cards/3-d.png"))
    d4 = ImageTk.PhotoImage(Image.open("C:/Users/Niki/Desktop/Olio-ohjelmointi/Images/cards/4-d.png"))
    d5 = ImageTk.PhotoImage(Image.open("C:/Users/Niki/Desktop/Olio-ohjelmointi/Images/cards/5-d.png"))
    d6 = ImageTk.PhotoImage(Image.open("C:/Users/Niki/Desktop/Olio-ohjelmointi/Images/cards/6-d.png"))
    d7 = ImageTk.PhotoImage(Image.open("C:/Users/Niki/Desktop/Olio-ohjelmointi/Images/cards/7-d.png"))
    d8 = ImageTk.PhotoImage(Image.open("C:/Users/Niki/Desktop/Olio-ohjelmointi/Images/cards/8-d.png"))
    d9 = ImageTk.PhotoImage(Image.open("C:/Users/Niki/Desktop/Olio-ohjelmointi/Images/cards/9-d.png"))
    d10 = ImageTk.PhotoImage(Image.open("C:/Users/Niki/Desktop/Olio-ohjelmointi/Images/cards/10-d.png"))
    d11 = ImageTk.PhotoImage(Image.open("C:/Users/Niki/Desktop/Olio-ohjelmointi/Images/cards/J-d.png"))
    d12 = ImageTk.PhotoImage(Image.open("C:/Users/Niki/Desktop/Olio-ohjelmointi/Images/cards/Q-d.png"))
    d13 = ImageTk.PhotoImage(Image.open("C:/Users/Niki/Desktop/Olio-ohjelmointi/Images/cards/K-d.png"))
    d14 = ImageTk.PhotoImage(Image.open("C:/Users/Niki/Desktop/Olio-ohjelmointi/Images/cards/A-d.png"))
    # Hearts
    h2 = ImageTk.PhotoImage(Image.open("C:/Users/Niki/Desktop/Olio-ohjelmointi/Images/cards/2-h.png"))
    h3 = ImageTk.PhotoImage(Image.open("C:/Users/Niki/Desktop/Olio-ohjelmointi/Images/cards/3-h.png"))
    h4 = ImageTk.PhotoImage(Image.open("C:/Users/Niki/Desktop/Olio-ohjelmointi/Images/cards/4-h.png"))
    h5 = ImageTk.PhotoImage(Image.open("C:/Users/Niki/Desktop/Olio-ohjelmointi/Images/cards/5-h.png"))
    h6 = ImageTk.PhotoImage(Image.open("C:/Users/Niki/Desktop/Olio-ohjelmointi/Images/cards/6-h.png"))
    h7 = ImageTk.PhotoImage(Image.open("C:/Users/Niki/Desktop/Olio-ohjelmointi/Images/cards/7-h.png"))
    h8 = ImageTk.PhotoImage(Image.open("C:/Users/Niki/Desktop/Olio-ohjelmointi/Images/cards/8-h.png"))
    h9 = ImageTk.PhotoImage(Image.open("C:/Users/Niki/Desktop/Olio-ohjelmointi/Images/cards/9-h.png"))
    h10 = ImageTk.PhotoImage(Image.open("C:/Users/Niki/Desktop/Olio-ohjelmointi/Images/cards/10-h.png"))
    h11 = ImageTk.PhotoImage(Image.open("C:/Users/Niki/Desktop/Olio-ohjelmointi/Images/cards/J-h.png"))
    h12 = ImageTk.PhotoImage(Image.open("C:/Users/Niki/Desktop/Olio-ohjelmointi/Images/cards/Q-h.png"))
    h13 = ImageTk.PhotoImage(Image.open("C:/Users/Niki/Desktop/Olio-ohjelmointi/Images/cards/K-h.png"))
    h14 = ImageTk.PhotoImage(Image.open("C:/Users/Niki/Desktop/Olio-ohjelmointi/Images/cards/A-h.png"))

    spades = [s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14]
    clubs = [c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14]
    diamonds = [d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12, d13, d14]
    hearts = [h2, h3, h4, h5, h6, h7, h8, h9, h10, h11, h12, h13, h14]

    # Builds deck and creates all the players
    deck = Deck()
    computer1 = Player("C1")
    computer2 = Player("C2")
    computer3 = Player("C3")

    players = [computer1, computer2, computer3, player]

    # create hands for all the players
    comp_c1 = []
    comp_c2 = []
    comp_c3 = []
    player_c = []
    players_cards = [comp_c1, comp_c2, comp_c3, player_c]



def dice_game():
    # function to get bet amount from entry box
    def game_bet():
        bet_size = int("%s" % (bet.get()))
        return bet_size

    # game main function
    def game():
        # rolling all the dices
        computer1.roll_dice()
        computer2.roll_dice()
        player1.roll_dice()
        player2.roll_dice()

        # getting dice values and adding them together
        computer_total = computer1.get_dice() + computer2.get_dice()
        player_total = player1.get_dice() + player2.get_dice()

        # checking who wins and adjust player money, also shows text whether you win, lose or tie
        if computer_total > player_total:
            player.set_money(player.get_money()-game_bet())
            lose_lbl.place(x=355, y=260)

        elif player_total > computer_total:
            player.set_money(player.get_money()+game_bet())
            win_lbl.place(x=355, y=260)

        else:
            tie_lbl.place(x=355, y=260)

        # show rolled dices

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

    # All the entry widgets
    bet = Entry(dice, width=12)
    bet.place(x=700, y=300)

    # All the texts
    bet_lbl = Label(dice, text="Your bet", font=('calibri', 16, 'bold'))
    bet_lbl.place(x=698, y=270)

    # All the buttons
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
player = Player("player")

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

from tkinter import *
from winsound import *
import string
import random

#creates window and title. add icon here
root = Tk()
root.title('Hatchegories')
root.geometry('700x500')

#letter, timer and list labels so they can be edited in following functions
letter_label1 = Label(root, text='Letter:', font=('Calibri', 15))
letter_label = Label(root, text=' ', font=('Calibri', 40))
timer_label = Label(root, text='Timer:\n', font=('Calibri', 20))
list_numbers = Label(root, text='1.\n2.\n3.\n4.\n5.\n6.\n7.\n8.\n9.\n10.\n11.\n12.', font=('Calibri', 14))
list_contents = Label(root, text='Welcome to Hatchegories!\n\nAll the categories and\nnone of the fuss.\n\nPress a button to begin.', justify=LEFT, font=('Calibri', 14))

#grid locations for the above
letter_label1.grid(row=0, column=0, padx=150, pady=10)
letter_label.grid(row=1, column=0, padx=150, pady=5)
timer_label.grid(row=2, column=0, padx=150, pady=30)
list_numbers.grid(row=0, column=1, rowspan=6)
list_contents.grid(row=0, column=2, rowspan=6)

#starts countdown timer
def countdown(count=180):
    timer_label['text'] = f'Timer:\n{count}'
    global gotimer
    if count > 0:
        # call countdown again after 1000ms (1s)
        gotimer = root.after(1000, countdown, count-1)
    else:
        timer_label['text'] = "Time's up!"
        play = lambda: PlaySound('buzz.wav', SND_FILENAME)
        play()

def reset_timer():
    #stops the after method, initializes text to ----
    root.after_cancel(gotimer)
    timer_label['text'] = 'Timer:\n----'

def random_letter():
    #creates 'Scattegories' alphabet
    alpha = list(string.ascii_uppercase)
    unwanted = ['Q', 'U', 'V', 'X', 'Y', 'Z']

    alpha = [letter for letter in alpha if letter not in unwanted]

    #generates random letter
    randletter = random.choice(alpha)

    #changes letter label
    letter_label.config(text=randletter)

def random_list():
    #opens list document and selects 12 items
    lists = open("lists.txt", encoding='utf-8').readlines()
    list12 = (random.sample(lists, 12))

    #strip removes \n character, then print each item on newline
    converted_list = []
    numbered_list = []

    for item in list12:
        converted_list.append(item.strip())

    list_contents.config(text=("\n".join(converted_list)))

#define all the objects in my window.
reset_timer_button = Button(root, text='Reset Timer', padx=25, font=('Calibri', 12), command=reset_timer)
start_timer_button = Button(root, text='Start Timer', padx=28, font=('Calibri', 12), command=countdown)
random_letter_button = Button(root, text='Random Letter', padx=17, font=('Calibri', 12), command=random_letter)
random_list_button = Button(root, text='Random List', padx=25, font=('Calibri', 12), command=random_list)
copyright = Label(root, text='by Grace Hatcher 2020', font=('Calibri', 10))

#where all the objects go in my window
reset_timer_button.grid(row=3, column=0, pady=5)
start_timer_button.grid(row=4, column=0, pady=5)
random_letter_button.grid(row=5, column=0, pady=5)
random_list_button.grid(row=6, column=0, pady=5)
copyright.grid(row=7, column=0, pady=5)

#keeps window open until it's closed
root.mainloop()

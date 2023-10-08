"""This project is done by a group of 2 members:
1. Mariam Mohamed Elwirish - 320220076
2. Yousef Mohamed Mohamed Hamed - 320220064"""
"""Note: This project needs an extra library to be installed 
(pyspellchecker, textblob, re (note: it will be automatically installed with textblob)).
Kindly make sure it's installed before running the code.
If still didn't work, kindly run the code from the cmd."""
import tkinter
import re
from tkinter import *
from spellchecker import SpellChecker
from textblob import TextBlob
window = Tk()
window.title("Spelling Checker")
window.geometry("700x400")
window.maxsize(700,400)
window.config(background="#26292c")


def check():
    spell_function = SpellChecker()
    case.config(text="")
    spell.config(text="")
    wrong.config(text="")
    word = writing.get()
    check_symbol = re.findall("[a-zA-Z ]+", word)
    updated = ("".join(check_symbol))
    word_list = list(updated.split(" "))
    misspelled = spell_function.unknown(updated.split(" "))
    if (len(word_list) == 1 and word_list[0] != '') or (len(word_list) == 2 and (word_list[0]=='' or word_list[1]=='')):
        if misspelled and misspelled != {''}:
            checking = TextBlob(updated)
            right = checking.correct()
            if checking.correct() != word and checking.correct() != updated:
                wrong.config(text="Wrong Spelling!")
                wrong.pack()
                case.config(text="Correct Spelling: ")
                case.place(x=250,y=200)
                spell.place(x=390,y=203)
                spell.config(text=right)
            else:
                case.config(text="Wrong word. Not found.")
                case.pack()
        else:
                case.config(text="Correct Word!")
                case.pack()
    elif len(word_list) == 1 and word_list[0] == '':
        case.config(text="Please Enter At Least One Word!")
        case.pack()
    else:
        case.config(text="Please Enter Only One Word!")
        case.pack()
    writing.delete(0, END)


Title = Label(window, text="Welcome to Spelling Checker!", font=("Cascadia Mono", 20, "bold"), bg="#26292c", fg="#baa054")
Title.pack(pady=10)
writing = Entry(window, justify="left", width=30, font=("Cairo", 10), bg="#9f9b95", border=1)
writing.pack(pady=10)
writing.focus()
Enter = Button(window, width=10, highlightcolor= "black", font=("Cascadia Mono", 10, "bold"), fg="#CBE4DE", bg="#5e7993" ,text= "Check",  command=check)
Enter.pack(pady=10)
wrong = Label(window, font=("Cairo", 15,"bold"), bg="#26292c", fg="#a25555")
case = Label(window, font=("Cairo", 15,"bold"), bg="#26292c", fg="#a25555")
spell = Label(window, font=("Cairo", 13), bg="#26292c", fg="#E4E4E4")
window.mainloop()
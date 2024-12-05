import sys
import random
import tkinter as tk
from tkinter import *
from tkinter import font

def read_data():
    with open(sys.argv[1], "r") as f:
        lines = [line.rstrip() for line in f]
    return lines

def next_question():
    global counter 
    counter = random.randint(0, len(task)-1)
    Q = task[counter].split("--")
    question.delete('1.0', END)
    answer.delete('1.0', END)  
    question.insert(END, Q[0])
    question.pack()

def answer_question():
    Q = task[counter].split("--")
    answer.insert(END, Q[1])
    answer.pack()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Physik-Quiz:")
    root.geometry("800x320")

    Font_tuple = ("Helvetica", 14, "bold") 

    counter = 0
    task = read_data()

    question = Text(root, height = 5, width = 52)
    question.configure(font = Font_tuple)
    answer = Text(root, height = 5, width = 52)
    answer.configure(font = Font_tuple) 

    question_button = tk.Button(
        root,
        text="Frage",
        command=next_question
        )
        
    answer_button = tk.Button(
        root,
        text="Antwort",
        command=answer_question
        )  
  
    question_button.pack()
    answer_button.pack()
    root.mainloop()

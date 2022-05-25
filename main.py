import tkinter as tk
import tkinter.ttk as ttk
from random import randint

window = tk.Tk()
window.title("Dice")
window.geometry("300x100")

display_number = tk.Label(window, text="", font=(200))

def roll_dice():
    number = randint(1, 6)
    display_number.configure(text=number)
    display_number.pack()

roll_btn = ttk.Button(window, text="Roll the dice!", command=roll_dice).pack()

window.mainloop()

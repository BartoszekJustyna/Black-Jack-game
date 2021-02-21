import tkinter as tk
import random

def display():
    x= ["1", "2", "3", "K", "D" "J"]
    name = random.choice(x)

    root = tk.Tk()
    h = 400
    w = 250

    card = tk.Canvas(root, height=h, width=w)
    card.pack()

    frame = tk.Frame(card, bg="#F16683")
    frame.place(relheight=0.8, relwidth=0.8, relx=0.1, rely=0.1)

    heart = tk.PhotoImage(file="heart.png")
    heart_label = tk.Label(frame, image=heart)
    heart_label.place(relheight=0.2, relwidth=0.4)

    heart_frame = tk.Entry(frame, bg="white")
    heart_frame.place(relheight=0.3, relwidth=0.3, relx=0.35, rely=0.35)

    name_card = tk.Message(heart_frame, text=f"{name}")
    name_card.place(relheight=0.8, relwidth=0.8, rely=0.1, relx=0.1)

    root.mainloop()

display()
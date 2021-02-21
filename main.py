import heart
import random

def color():
    colors = ["heart.png", "pik.png", "trefl.png", "karo.png" ]
    return random.choice(colors)

def name():
    y= ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "D", "K", "A"]
    return random.choice(y)


heart.heart_card(name(), color())
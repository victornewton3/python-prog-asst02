from microbit import *

eye1 = Image("09990:"
             "90909:"
             "09990:"
             "00000:"
             "00000")

eye2 = Image("09990:"
             "90909:"
             "09990:"
             "00900:"
             "00000")

eye3 = Image("09990:"
             "90909:"
             "09990:"
             "00000:"
             "00900")

eye4 = Image("09990:"
             "90909:"
             "09990:"
             "00000:"
             "00000")

all_eyes = [eye1, eye2, eye3,eye4]
display.show(all_eyes,loop=True, delay=200)
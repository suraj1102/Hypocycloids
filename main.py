from tkinter import *
from time import sleep
from math import cos, sin
from random import random

def main(enter):
    root = Tk()
    root.title('Hypocloid')
    canvas = Canvas(root, width=1000, height=1000, bg='white')
    canvas.pack()
    root.resizable(True, True)

    t = 0
    step = 0.1
    scale = 4
    r = 10

    if enter == 'r':
        k = round((random() * 20) - 10, 1)
    else:
        k = float(enter)
    R= k*r
    print('\nK = ' + str(k))

    canvas.create_text(100,50,font=10, text=('k = ' + str(k)))
    canvas.create_oval(500 - R*5, 500 - R*5, 500 + R*5, 500 + R*5, width=3)

    while True:
        try:
            x1 = (r * (k - 1)) * (cos(t) + (cos(t * (k - 1)) / (k - 1)))
            y1 = (r * (k - 1)) * (sin(t) - (sin(t * (k - 1)) / (k - 1))) 


            x2 = (r * (k - 1)) * (cos(t + step) + (cos((t + step) * (k - 1)) / (k - 1)))
            y2 = (r * (k - 1)) * (sin(t + step) - (sin((t + step) * (k - 1)) / (k - 1))) 
        except ZeroDivisionError:
            print('Zero Division Attempt')
            root.destroy()
            input()
            break

        canvas.create_line(x1 * 5 + 500, y1 * 5 + 500, x2 * 5 + 500, y2 * 5 + 500, fill='red', width=2)
        canvas.update()
        t += step
        sleep(0.005)

root = Tk()
my_entry = Entry(root, text='k = ')
my_button = Button(root, text='Run', command = lambda: main(my_entry.get()))

my_entry.pack()
my_button.pack()

root.mainloop()

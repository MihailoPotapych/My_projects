from tkinter import *
import random
window=Tk()
window.geometry("700x532")
window.title('Кликер')
colors = ['black', 'white', 'red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
cnt = 0

def ChangeColor():
    color = random.choice(colors)
    if color == 'black':
        butt['fg'] = 'white'
    else:
        butt['fg'] = 'black'
    butt['background'] = color

def ChangeLabelColor():
    color = random.choice(colors)
    if color == 'black':
        score_label['fg'] = 'white'
    else:
        score_label['fg'] = 'black'
    score_label['bg'] = color

def onClick():
    global  cnt
    butt.place(x=random.randint(0,700-105), y=random.randint(41,500-28))
    cnt += 1
    score_label['text'] = f'Счет: {cnt}'
    if cnt % 10 == 0:
        ChangeColor()
    ChangeLabelColor()

butt = Button(text='Нажми меня!', font=('Arial', 12), command=onClick)
butt.place(x=300, y=200, width=105, height=28)

score_label = Label(text='Счет: 0', font=('Arial', 24), bg='blue')
score_label.pack()

window.mainloop()
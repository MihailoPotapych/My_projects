from tkinter import *
import random as r

w=600
h=600

window = Tk()
window.geometry(f'{str(w)}x{str(h)}')
window.title('Game')

c = Canvas(window, width=w, height=h, bg='white')
c.pack()

bg_photo = PhotoImage(file='img/background.png')

class Knight:
    def __init__(self):
        self.x = 70
        self.y = h//2
        self.v = 0
        self.photo = PhotoImage(file='img/knight.png')
    def up(self, event):
        self.v = -3
    def down(self, event):
        self.v = 3
    def stop(self, event):
        self.v = 0

class Dragon:
    def __init__(self):
        self.x = 750
        self.y = r.randint(100, 500)
        self.v = r.randint(1, 3)
        self.photo = PhotoImage(file='img/dragon.png')

knight = Knight()

dragons = []
for i in range(3):
    dragons.append(Dragon())

def game():
    c.delete('all')
    c.create_image(300, 300, image = bg_photo)
    knight.y += knight.v
    c.create_image(knight.x, knight.y, image = knight.photo)

    curr_d = 0
    d_kll = -1

    for dragon in dragons:
        dragon.x -= dragon.v
        c.create_image(dragon.x, dragon.y, image = dragon.photo)
        if((dragon.x-knight.x)**2+(dragon.y-knight.y)**2) <= 96**2:
            d_kll = curr_d

        curr_d += 1

        if dragon.x <=0:
            c.delete('all')
            c.create_text(w // 2, h // 2, text='Game over!', font=('Arial', 40), fill='red')
            break
    if d_kll >= 0:
        del dragons[d_kll]

    if len(dragons) == 0:
        c.delete('all')
        c.create_text(w//2, h//2, text='You win!', font=('Arial', 40), fill='red')
    else:
        window.after(50, game)

window.bind('<Key-Up>', knight.up)
window.bind('<Key-Down>', knight.down)
window.bind('<KeyRelease>', knight.stop)

game()
window.mainloop()
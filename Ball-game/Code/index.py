from tkinter import *
import random

w = Tk()
w.title('Ball')
w.resizable(width=False, height=False)

c = Canvas(width=500, height=400, bg='green',highlightthickness=0)
c.pack()


class Racket:
    def __init__(self):
        self.racket = c.create_rectangle(230, 300, 330, 310, fill='black')
        self.v = 0
        self.x = 500 // 2

    def right(self, e):
        self.v = 2

    def left(self, e):
        self.v = -2

    def stop(self, e):
        self.v = 0

    def draw(self):
        coord = c.coords(self.racket)[0]
        if coord == 402:
            c.move(self.racket, -2, 0)
        elif coord == -2:
            c.move(self.racket, 2, 0)
        else:
            c.move(self.racket, self.v, 0)


class Ball:
    def __init__(self):
        self.ball = c.create_oval(200, 100, 215, 115, fill='red', outline='')
        self.curr_direct = random.choice([[1, -1], [1, 1], [-1, -1], [-1, 1]])
        self.coords = c.coords(self.ball)
        self.tch = False

    def was_touch(self):
        r_coords = c.coords(racket.racket)
        if self.coords[3] >= 400:
            return None
        if self.coords[0] <= 0 or self.coords[1] <= 0 or self.coords[2] >= 500:
            self.tch = True
            return 0
        if self.coords[2] >= r_coords[0] and self.coords[0] <= r_coords[2]:
            if self.coords[3] >= r_coords[1] and self.coords[3] <= r_coords[3]:
                self.tch = True
                return 0
        self.tch = False
        return 0

    def change_direction(self):
        if self.coords[0] <= 0:
            if self.curr_direct == [-1, -1]:
                self.curr_direct = [1, -1]
                return
            else:
                self.curr_direct = [1, 1]
                return
        if self.coords[2] >= 500:
            if self.curr_direct == [1, 1]:
                self.curr_direct = [-1, 1]
                return
            else:
                self.curr_direct = [-1, -1]
                return
        if self.coords[1] == 0:
            if self.curr_direct == [-1, -1]:
                self.curr_direct = [-1, 1]
                return
            else:
                self.curr_direct = [1, 1]
                return
        if self.coords[3] <= 300:
            if self.curr_direct == [-1, 1]:
                self.curr_direct = [-1, -1]
            else:
                self.curr_direct = [1, -1]

    def draw(self):
        c.move(self.ball, self.curr_direct[0], self.curr_direct[1])


racket = Racket()
ball = Ball()


def game():
    racket.draw()
    ball.coords = c.coords(ball.ball)
    if ball.was_touch() is None:
        c.delete('all')
        c.create_text(500 // 2, 400 // 2, text='Game over!', font=('Arial', 40), fill='red')
        return
    if ball.tch:
        ball.change_direction()
    ball.draw()
    w.after(6, game)


w.bind('<Key-Right>', racket.right)
w.bind('<Key-Left>', racket.left)
w.bind('<KeyRelease>', racket.stop)

game()

w.mainloop()
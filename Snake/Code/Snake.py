from tkinter import *
import random as r
import sys

size = 20
tick = 100
width = size*20
height = size*20+40
w = Tk()
w.geometry(f'{width}x{height}')
w.resizable(width=False, height=False)
w.title('Змейка')


class Head:
    def __init__(self):
        self.head = canvas.create_rectangle(size*4, size, size*5, size*2, fill='red', outline='')
        self.coords = canvas.coords(self.head)
        self.v = size
        self.vector = [1, 0]
        self.old_vectors = [[1, 0], [1, 0], [1, 0]]
        self.score = 0
        self.was_press = 0
        self.directions_list = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        self.future_vectors = []
        self.stop = False

    def move(self, tail, score, food=None):
        l = ['Up', 'Down', 'Left', 'Right']
        if self.was_press >= 2:
            direction_index = self.directions_list.index(self.old_vectors[0])
            conflict_vector = self.directions_list[direction_index + (1 if direction_index % 2 == 0 else -1)]
            if self.vector == conflict_vector:
                self.future_vectors = self.old_vectors[1:]
            if self.old_vectors[0] == self.old_vectors[-1]:
                self.future_vectors = self.old_vectors[1:]


        if self.future_vectors != []:
            self.change_direction(self.directions_list.index(self.future_vectors[0]), False)
            del self.future_vectors[0]
        elif self.was_press >= 2:
            pass



        self.was_press = 0
        self.coords = canvas.coords(self.head)
        new_coords = self.coords[0] + self.vector[0] * self.v, self.coords[1] + self.vector[1] * self.v
        new_coords = new_coords[0], new_coords[1], new_coords[0]+size, new_coords[1]+size
        if self.is_game_over(new_coords, tail):
            game_over(score, self, food)
        else:
            canvas.coords(self.head, new_coords[0], new_coords[1], new_coords[2], new_coords[3])

    def is_game_over(self, coords, tail):
        return is_belong_tail([coords[0], coords[1]], tail, [-1, -1]) \
            or coords[0] < 0 or coords[1] < 0 or coords[2] > width or coords[3] > height-40

    def change_direction(self, direction_index, button=True):
        ignore_change = True
        if ignore_change:
            new_direction = self.directions_list[direction_index]
            conflict_direction = self.directions_list[direction_index + (1 if direction_index % 2 == 0 else -1)]
            if self.vector != conflict_direction:
                self.vector = new_direction
                if button:
                    self.was_press += 1
                if len(self.old_vectors) <= 2:
                    self.old_vectors.append(self.vector)
                else:
                    del self.old_vectors[0]
                    self.old_vectors.append(self.vector)


class Tail:
    def __init__(self, x, y):
        colors_list = ['yellow', 'blue', 'violet', 'white', 'green', 'gray', 'magenta', 'pink']
        clr = r.choice(colors_list)
        self.elem = canvas.create_rectangle(x, y, x + size, y + size, fill=clr, outline='')
        self.coords = canvas. coords(self.elem)

    def update_coords(self):
        self.coords = canvas.coords(self.elem)

    def move(self, delta):
        canvas.coords(self.elem, delta[0], delta[1], delta[0] + size, delta[1] + size)


class Food:
    def __init__(self):
        self.food = None
        self.coords = None

    def suppose(self):
        x = r.randint(0, (20-1)*size)
        y = r.randint(0, (20-1)*size)
        return [x - x % size, y - y % size]

    def generate_food(self, tail, head_coords):
        food_pose = self.suppose()
        while is_belong_tail(food_pose, tail, head_coords):
            food_pose = self.suppose()
        self.draw(food_pose)

    def draw(self, pose):
        self.food = canvas.create_rectangle(pose[0], pose[1], pose[0]+size, pose[1]+size, fill='orange', outline='')
        self.coords = canvas.coords(self.food)

    def delete(self):
        canvas.delete(self.food)


def begin():
    canvas.delete('all')
    score_label['text'] = 'Счет: 0'
    replay_button.place_forget()
    begin_button.destroy()
    score_label.place(x=0, y=0, width=width+1, height=40)

    score = 0
    head = Head()
    tail = [Tail(x, size) for x in range(size, size*3+1, size)]
    food = Food()

    w.bind('<Key-Up>', lambda e: head.change_direction(0))
    w.bind('<Key-Left>', lambda e: head.change_direction(2))
    w.bind('<Key-Down>', lambda e: head.change_direction(1))
    w.bind('<Key-Right>', lambda e: head.change_direction(3))

    w.bind('<w>', lambda e: head.change_direction(0))
    w.bind('<a>', lambda e: head.change_direction(2))
    w.bind('<s>', lambda e: head.change_direction(1))
    w.bind('<d>', lambda e: head.change_direction(3))

    main(head, tail, food, score)


def main(head, tail, food, score):
    tail[-1].update_coords()
    head.move(tail, score, food)
    if head.stop:
        return
    old_head = head.coords[0], head.coords[1]
    old_last_tail = tail[0].coords
    tail[0].move(old_head)
    tail.append(tail.pop(0))
    if head.coords == food.coords:
        food.delete()
        score += 1
        score_label['text'] = score_label['text'].replace(str(score-1), str(score))
        tail.insert(0, Tail(old_last_tail[0], old_last_tail[1]))
        food.generate_food(tail, head.coords)
    if food.food is None:
        food.generate_food(tail, head.coords)
    w.after(tick, lambda: main(head, tail, food, score))


def is_belong_tail(coords, tail, head):
    for t in tail:
        if coords == [t.coords[0], t.coords[1]] or coords == [head[0], head[1]]:
            return True
    return False


def game_over(score, head, food):
    head_coords, food_coords = head.coords, food.coords
    head.stop = True
    if head_coords == food_coords:
        score += 1
        food.delete()
    score_label['text'] = f'Вы проиграли! Ваш счет: {score}'
    replay_button.place(x=width//2-159//2, y=height//2-47//2)


begin_button = Button(text='Играть!', bg='red', fg='white', font=('Arial', 24), command=begin)
begin_button.place(x=0, y=0, width=width, height=40)
score_label = Label(text='Счет: 0', bg='red', fg='white', font=('Arial', 20))
canvas = Canvas(bg='black', highlightthickness=0)
canvas.place(x=0, y=40, width=width+1, height=height-40)
replay_button = Button(text='Переиграть!', font=('Arial', 18), command=begin)


w.mainloop()

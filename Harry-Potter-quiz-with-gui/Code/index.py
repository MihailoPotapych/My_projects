import random
from tkinter import *
window = Tk()
window.geometry("710x350")#384*333
window.title('Тест')

questions = [
    {
        'question': 'Мальчик-Который-Выжил - это...',
        'answers': ['Гарри Поттер', 'Рональд Уизли', 'Драко Малфой']},

    {
        'question': 'Кто из персонажей является оборотнем?',
        'answers': ['Римус Люпин', 'Сириус Блэк', 'Том Реддл']},

    {
        'question': 'Кто не предавал Волан-де-Морта?',
        'answers': ['Беллатриса Лестрейндж', 'Северус Снегг', 'Регулус Блэк']},

    {
        'question': 'Как зовут феникса Дамблдора?',
        'answers': ['Фоукс', 'Файрекс', 'Финикс']},

    {
        'question': 'Кто из перечисленных персонажей лучше играет в шахматы?',
        'answers': ['Рон', 'Гермиона', 'Гарри']},
    {
        'question': 'Кагого цвета глаза Гарри Поттера(в книге)?',
        'answers': ['Зелёного', 'Синего', 'Серого']},

    {
        'question': 'Какую форму имеет Патронус Гарри Поттера?',
        'answers': ['Олень', 'Выдра', 'Феникс']},

    {
        'question': 'Кто убил Беллатрису Лестрейндж?',
        'answers': ['Молли Уизли', 'Гарри Поттер', 'Джинни Уизли']},

    {
        'question': 'Как зовут кошку Филча?',
        'answers': ['Миссис Норрис', 'У Филча не было кошки', 'Мурка']},

    {
        'question': 'Настоящее имя Волан-де-Морта - это...',
        'answers': ['Том Реддл', 'Геллерт Гриндевальд', 'Квиринус Квиррелл']}

]

quest_num = 0
score = 0
entryVar = StringVar()
right_ans = 0
OldResult = ''
skipAnsRand = False

def showEnter_err():
    global  quest_num, skipAnsRand
    err_label['text'] = 'Пожалуйста, введите корректное значение'
    skipAnsRand = True

def IsInt(inp):
    try:
        int(inp)
        return True
    except BaseException:
        return False

def SecondCheckInp(inp, maxVal):
    if (int(inp) <= maxVal)and(int(inp) > 0):
        return inp
    else:
        showEnter_err()
        inp = entry.get()


def CheсkInp(inp):
    global  skipAnsRand
    if IsInt(inp):
        err_label['text'] = ''
        skipAnsRand = False
        return SecondCheckInp(inp, 3)
    else:
        showEnter_err()
        inp = entry.get()

def closeWindow():
    window.destroy()

def showFinalScreen():
    title_label['text'] = 'Спасибо за прохождение!'
    label1['text'] = f'Ваш счет: {score}'
    entry.destroy()
    label2.destroy()
    err_label.destroy()
    butt['text'] = 'Выход'
    butt['command'] = closeWindow

def getLabelText():
    global quest_num, right_ans, OldResult, skipAnsRand
    if quest_num == len(questions):
        showFinalScreen()
        return
    if skipAnsRand == True:
        quest_num -= 1
        return  OldResult
    if quest_num != 0:
        title_label['text'] = f'Вопрос №{quest_num + 1}'
    result = questions[quest_num]['question'] + '\n'*2
    elem_index_values = []

    for ans_num in range(1, len(questions[quest_num]['answers'])+1):
        elem_index = random.randint(0, len(questions[quest_num]['answers']) - 1)

        while True:
            if elem_index in elem_index_values:
                elem_index = random.randint(0, len(questions[quest_num]['answers']) - 1)
            else:
                break

        elem_index_values.append(elem_index)

        if elem_index == 0:
            right_ans = ans_num
        ans = questions[quest_num]['answers'][elem_index]

        result += str(ans_num) + '.' + ans
        if ans_num < len(questions[quest_num]['answers']):
            result += '\n'
    OldResult = result
    return result

def hideFirstScreen():
    title_label['text'] = 'Вопрос №1'
    label1.place(x=10, y=50)
    label2.place(x=17, y=197)
    entry.place(x=17, y=230)
    entry.focus()
    err_label.place(x=15, y=261)
    butt.place(x=62, y=285)
    butt['text'] = 'Ответить'
    butt['command'] = checkAnswer

def checkAnswer():
    global quest_num, score, right_ans
    user_ans = CheсkInp(entry.get())
    entry.delete(0, END)
    if user_ans == str(right_ans):
        score += 1

    if quest_num < len(questions):
        quest_num += 1
        label1['text'] = getLabelText()
    else:
        points_label=Label(text='Вы получили' + str(score) + ' очков(а)', font=('Arial', 24), bg='red', fg='white')
        points_label.place(x=0, y=0, width=700, height=50)


title_label = Label(text='Тест по теме "Гарри Поттер"', font=('Arial', 24), bg='red', fg='white')
title_label.place(x=0, y=0, width=710, height=50)

label1 = Message(text=getLabelText(),font=('Arial', 18), width=690)

label2 = Label(text='Введите номер ответа:', font=('Arial', 17))

entry = Entry(font=('Arial', 18))

err_label = Label(text='', font=('Arial', 10), fg='red')

butt = Button(text='Начать', font=('Arial', 24), command=hideFirstScreen)
butt.place(x=272.5, y=285)#butt.place(x=62, y=285)

window.mainloop()
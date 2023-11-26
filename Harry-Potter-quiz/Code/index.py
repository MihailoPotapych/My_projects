import random

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
        'question': 'Должность преподавателя какого предмета в Хогвартсе считалась проклятой?',
        'answers': ['Защита от темных искусств', 'Трансфигурация', 'Зельеварение']},
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

print('*' * 20 + ' Викторина на тему "Гарри Поттер" ' + '*' * 20 + '\n')

Name = input('Введите ваше имя: ')

ShowRightAns = input('Хотите ли вы, чтобы при вводе неверного ответа отображался верный?(да или нет):\n').lower()
NumCorrAns = 0

while True:
    if (ShowRightAns == 'да') or (ShowRightAns == 'нет'):
        break
    else:
        ShowRightAns = input('Пожалуйста, введите корректное значение: ').lower()
print('\n')

for quest in questions:
    print('Вопрос №' + str(questions.index(quest) + 1) + '. ' + quest['question'])
    elem_index_values = []
    right_ans = 0
    for ans_num in range(1, len(quest['answers']) + 1):
        elem_index = random.randint(0, len(quest['answers']) - 1)

        while True:
            if elem_index in elem_index_values:
                elem_index = random.randint(0, len(quest['answers']) - 1)
            else:
                break

        elem_index_values.append(elem_index)

        if elem_index == 0:
            right_ans = ans_num
        ans = quest['answers'][elem_index]

        print(str(ans_num) + '.', ans)

    user_ans = input('Введите номер ответа: ')
    while True:
        try:
            int(user_ans)
        except BaseException:
            user_ans = input('Пожалуйста, введите числовое значение: ')
        if int(user_ans) in range(1, len(quest['answers']) + 1):
            break
        else:
            user_ans = input('Пожалуйста, введите корректное значение: ')

    if int(user_ans) == right_ans:
        print('Верно!\n')
        NumCorrAns += 1
    else:
        if ShowRightAns == 'да':
            print('Неверно. Правильный ответ: ' + str(right_ans) + '.\n')
        else:
            print('Неверно.\n')

    if questions.index(quest) + 1 == len(questions):
        print('Правильных ответов ' + str(NumCorrAns * 10) + '%.')
        print('*' * 20 + ' Спасибо за прохождение! ' + '*' * 20)

file = open('result.txt', 'a')
file.write(Name + " набрал " + str(NumCorrAns) + " баллов.\n")

print('Результаты других игроков:\n')

file = open('result.txt', 'r')

for string in file.readlines():
    print(string + '\n')

file.close()

closeVar = input('Нажмите <Enter> для продолжения...')

file.close()
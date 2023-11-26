import os
import argparse as ap
from getpass import getpass
from constants import abs_path as a_p
from constants import DISCIPLINES, HELPS
from constants import DISCIPLINES_PSEUDONYMS as D_P
from get_parse_data import get_list_of_disciplines_and_marks
from working_with_DB import update, get_all_on_date, get_all_on_discipline, update_user_data

def save_user_data():
    print('Обновление базы данных не может быть выполнено, так как ваши учетные данные не сохранены или сохранены неверно.')
    answer = input('Отправьте "0", чтобы записать (перезаписать) учетные данные, или "1", чтобы выйти: ')
    if answer == '0':
        auth = {'login': input('Введите логин: '), 'password': getpass('Введите пароль: ')}
        update_user_data(auth)
        print('Данные сохранены!')
        return True
    else:
        return False

def print_one_disc(disc, one):
    if one:
        if not disc.lower().startswith('информатика'):
            disc = disc[0].upper() + disc[1:].lower()
    print(f"{disc.replace('_', ' ') if disc != 'Информатика_и_ИКТ' else disc[:11]}:")
    marks = ''
    marks_list = []
    for mark in get_all_on_discipline(disc):
        if mark[0]:
            [marks_list.append(int(e)) for e in mark[0]]
            if len(mark[0]) == 1:
                marks += f' {mark[0]}'
            else:
                marks += ''.join([f' {e}' for e in mark[0]])
    print(marks if marks else ' Оценок нет')
    if marks:
        print(f'  Средний балл: {round(sum(marks_list)/len(marks_list), 2)}')
    return 1 if not marks else 0

def method_1(arguments):
    discipline = arguments[arguments.find('_')+1:].lower()
    discipline = D_P[discipline] if discipline in D_P else discipline
    if discipline == 'all':
        empty = 0
        for disc in DISCIPLINES:
            empty += print_one_disc(disc, False)
        if empty == 16:
            print('\nВозможно, база данных пуста. Попробуйте обновить ее с помощью команды /update.')
    elif discipline[0].upper() + discipline[1:].lower() in DISCIPLINES \
            or discipline.lower().startswith('информатика'):
        print_one_disc(discipline, True)
    else:
        print(f'Предмет {discipline} не распознан')

def method_2():
    raw_data = get_all_on_date()
    not_empty = False
    for line in raw_data:
        date = line[0]
        date = date[date.find('-')+1:] + '.' + date[:date.find('-')]
        print(f"Дата: {date.replace('-', '.')}")
        for e in enumerate(line[1:]):
            i, mark = e[0], e[1]
            if mark:
                out_mark = mark if len(mark) == 1 else f'{mark[0]}/{mark[1]}'
                print(f" {DISCIPLINES[i].replace('_', ' ')}: {out_mark}")
                not_empty = True
    if not not_empty:
        print('Возможно, база данных пуста. Попробуйте обновить ее с помощью команды /update.')

def show(arguments):
    if '_' in arguments:
        method = arguments[:arguments.find('_')]
    else:
        method = arguments
    if method == '1':
        method_1(arguments)
    elif method == '2':
        method_2()
    else:
        print(f'Формат вывода "{method}" не распознан')

def help(arg=None):
    if not arg:
        print(HELPS['base_help'])
    elif arg in list(HELPS.keys()):
        if arg != 'pseudonyms':
            print(HELPS[arg])
        else:
            HELPS[arg]()
    else:
        print(HELPS['commands'][arg])

def update_db():
    value = get_list_of_disciplines_and_marks()
    if value and type(value) == dict:
        update(value)
    elif save_user_data():
        update(get_list_of_disciplines_and_marks())
    else:
        return True
    print('База данных обновлена!')

def do(args):
    dop_args = args.dop_params if args.dop_params else None
    if dop_args:
        actions[args.action](dop_args)
    else:
        actions[args.action]()

actions = {
    '/help': lambda arg=None: help(arg),
    '/show': lambda arguments: show(arguments),
    '/update': update_db
}

parser = ap.ArgumentParser(description=HELPS['parser']['parser'])
parser.add_argument('action', default='/help', type=str, help=HELPS['parser']['action'])
parser.add_argument('-d-p', '--dop-params', type=str, help=HELPS['parser']['params'])

def folder_control():
    path = a_p('data')
    if not os.path.exists(path):
        os.mkdir(path)

def main():
    args = parser.parse_args()
    if args.action:
        folder_control()
        do(args)
    else:
        print('Ошибка: не указан обязательный параметр action.')

if __name__ == '__main__':
    print(a_p(''))
    main()
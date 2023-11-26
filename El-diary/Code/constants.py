from sys import executable as PATH

DISCIPLINES = [
    'Алгебра',
    'Английский_язык',
    'Биология',
    'География',
    'Геометрия',
    'Информатика_и_ИКТ',
    'История',
    'Литература',
    'Обществознание',
    'ОБЖ',
    'Родная_литература',
    'Русский_язык',
    'Технология',
    'Физика',
    'Физическая_культура',
    'Химия'
]


class Disciplines_pseudonyms:
    dict = {
        'английский': 'Английский_язык',
        'информатика': 'Информатика_и_ИКТ',
        'литра': 'Литература',
        'общество': 'Обществознание',
        'рлитра': 'Родная_литература',
        'русский': 'Русский_язык',
        'физра': 'Физическая_культура'
    }
    lst = list(dict.keys())
    def __getitem__(self, key):
        return self.dict[key]

    def __iter__(self):
        for e in self.lst:
            yield e
    

DISCIPLINES_PSEUDONYMS = Disciplines_pseudonyms()

def print_pseudonyms():
    print('К некоторым предметам можно обращаться не по полным именам, а по псевдонимам.')
    print('Список доступных псевдонимов:\n')
    for key, value in DISCIPLINES_PSEUDONYMS.dict.items():
        print(f'{value} <===> {key}')

HELPS = {
'parser': {
    'parser': 'Это консольный мини-интерфейс для электронного журнала на базе сайта https://sh-open.ris61edu.ru/.',
    'action': 'Действие, которое надо совершить. Чтобы вывести справку по доступным действиям, отправьте команду /help. Обязательный параметр.',
    'params': 'Параметры команды. Для получения подробной информации о дополнительных параметрах отправьте: "/help -d-p dop_params'
    },
'base_help':
    'Список доступных действий:\n'
    '  /help - выводит справочную информацию\n'
    '  /update - обновляет базу данных\n'
    '  /show - выводит информацию об оценках\n'
    'Для получения справки о конкретной команде введите команду /help с именем нужной команды в качестве параметра.'
    'Для получения справки о дополнительных параметрах введите: "/help -d-p dop_params"',
'commands': {
    'help':
        'Выводит справку. При вызове без аргументов выводится общая справка по командам.\n'
        'При вызове с аргументом, являющимся именем какой-либо команды, выводит справку по этой команде',
    'show':
        'Информация об оценках может быть выведена в следующих форматах:\n'
        '\nПервый (1):\n\nПредмет:\n'
        ' все оценки по предмету\n'
        '\n'
        'Предмет:\n'
        ' все оценки по предмету\n'
        '\n...\n'
        '\n2.Второй (2):\n\nДата:\n'
        ' Предмет: оценка\n'
        ' Предмет: оценка\n'
        '\n'
        'Дата:\n'
        ' Предмет: оценка\n'
        ' Предмет: оценка\n'
        ' \n...\n'
        '\n'
        'Как пользоваться: /show -d-p [метод вывода (1 или 2)]_[имя предмета или значение "all" (если метод вывода - 1)]\n'
        'Значение "all" позволяет вывести все оценки по всем предметам. В полных именах предметов надо ставить нижние подчеркивания ("_") вместо пробелов.\n'
        'К некоторым предметам можно обращаться по псевдонимам. Для получения справки о псевдонимах введите: "/help -d-p pseudonyms"\n'
        'Примеры:\n'
         '/show -d-p 2'+' '*10+'Вывод данных об оценках методом 2 (по датам)\n'
         '/show -d-p 1_all'+' '*10+'Вывод данных об оценках по всем предметам методом 1\n'
         '/show -d-p 1_русский_язык'+' '*10+'Вывод данных об оценках по русскому языку с указанием полного имени\n'
         '/show -d-p 1_русский'+' '*10+'Использование псевдонима',
    'update':
        'Обновляет локальную базу данных оценок в соответствии с информацией с сайта. Не имеет параметров.'
    },
'dop_params':
    'Дополнительные параметры команд - информация, предоставляемая командам для их корректной работы. Записываются после флага "-d-p", например: "/help update" - вызов команды "/help" с параметром "update"'
    'Некоторые команды не имеют параметров или могут вызываться без них, для некоторых команд дополнительные параметры обязательны (подробнее - см. справку о конкретных командах).',
'pseudonyms':
    print_pseudonyms
}

def abs_path(path):
    return PATH[:PATH.rfind('\\')+1]+path
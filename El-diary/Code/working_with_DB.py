import sqlite3 as sql
from datetime import datetime
from constants import abs_path as a_p

PATH = a_p(r'data\journal.db')
def init(crs, cnn):
    init_table_journal = """
    CREATE TABLE IF NOT EXISTS journal (
    Дата TEXT,
    Алгебра TEXT,
    Английский_язык TEXT,
    Биология TEXT,
    География TEXT,
    Геометрия TEXT,
    Информатика_и_ИКТ TEXT,
    История TEXT,
    Литература TEXT,
    Обществознание TEXT,
    ОБЖ TEXT,
    Родная_литература TEXT,
    Русский_язык TEXT,
    Технология TEXT,
    Физика TEXT,
    Физическая_культура TEXT,
    Химия TEXT
    )
    """
    init_table_user_data = """
    CREATE TABLE IF NOT EXISTS user_data (
    login TEXT,
    password TEXT
    )
    """
    init_user_data_fields = """
    INSERT INTO user_data VALUES (NULL, NULL)
    """
    crs.execute(init_table_journal)
    cnn.commit()
    crs.execute(init_table_user_data)
    cnn.commit()
    if len(get_user_data()) == 0:
        crs.execute(init_user_data_fields)
    cnn.commit()

def clear(cnn, crs):
    cmm = """
    DELETE FROM journal;
    """
    crs.execute(cmm)
    cnn.commit()

def update_user_data(auth):
    cmm = """
    UPDATE user_data SET (login, password) = (?, ?)
    """

    with sql.connect(PATH) as cnn:
        while True:
            try:
                crs = cnn.cursor()
                crs.execute(cmm, (auth['login'], auth['password']))
                cnn.commit()
                break
            except sql.OperationalError:
                init(crs, cnn)

def get_user_data():
    cmm = """
    SELECT * FROM user_data
    """
    with sql.connect(PATH) as cnn:
        while True:
            try:
                return cnn.execute(cmm).fetchall()
            except sql.OperationalError:
                init(cnn.cursor(), cnn)


def add_mark(cursor, cnn, dict):
    add_new_date = """
    INSERT INTO journal (Дата) VALUES (?)
    """
    add_new_mark = f"""
    UPDATE journal SET {str(list(dict.keys())[0]).replace(' ', '_')} = ?
    WHERE Дата = ?;
    """
    check_dates = """
    SELECT Дата FROM journal
    """
    check_cell = f"""
    SELECT {str(list(dict.keys())[0]).replace(' ', '_')} FROM journal
    WHERE Дата = ?;
    """
    date_and_mark = list(list(dict.values())[0].items())
    data = date_and_mark[0][0], date_and_mark[0][1]
    if not (data[0],) in cursor.execute(check_dates).fetchall():
        cursor.execute(add_new_date, (data[0],))
        cnn.commit()
    old_value = cursor.execute(check_cell, (data[0],)).fetchall()[0][0]
    if old_value:
        cursor.execute(add_new_mark, (int(str(old_value)+str(data[1])), data[0]))
    else:
        cursor.execute(add_new_mark, (data[1], data[0]))
    cnn.commit()

def get_all_on_discipline(discipline):
    cmm = f"""
    SELECT {discipline} FROM journal
    """
    with sql.connect(PATH) as cnn:
        while True:
            try:
                return cnn.execute(cmm).fetchall()
            except sql.OperationalError:
                init(cnn.cursor(), cnn)

def get_all_on_date():
    cmm = """
    select * from journal
    """
    with sql.connect(PATH) as cnn:
        while True:
            try:
                return cnn.execute(cmm).fetchall()
            except sql.OperationalError:
                init(cnn.cursor(), cnn)

def update(lst):
    with sql.connect(PATH) as cnn:
        cursor = cnn.cursor()
        clear(cnn, cursor)
        init(cursor, cnn)
        ordered_marks_data = []
        for dict in lst:
            discipline = list(dict.keys())[0]
            for m_d in dict[discipline]:
                ordered_marks_data.append({discipline: m_d})
        ordered_marks_data = sorted(ordered_marks_data, key=lambda x: list(x[list(x.keys())[0]].keys())[0])
        for mark_data in ordered_marks_data:
                add_mark(cursor, cnn, mark_data)

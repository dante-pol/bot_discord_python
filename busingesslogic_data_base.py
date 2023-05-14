import sqlite3
import datetime

connect = sqlite3.connect("firtst_sql.db")

cursor = connect.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS `timetable` (
id INTEGER NOT NULL PRIMARY KEY,
data TEXT NOT NULL,
time TEXT NOT NULL
);
""")
connect.commit()

def start():
    connect = sqlite3.connect("firtst_sql.db")
    cursor = connect.cursor()

def insert_date_lesson(*args):
    cursor.execute(f"""
            INSERT INTO `timetable` VALUES
                ({args[0]}, {args[1]});
        """)
    connect.commit()
    return "Данные вставлены"


def get_date_of_all_lesson():
    res = cursor.execute("SELECT `data`, `time` FROM `timetable`;")
    lstDateTime = res.fetchall()
    str = ''

    for i in lstDateTime:
        str += f"""Занятие по изучению языка Python состоится {i[0]} в {i[1]}.\n"""
    return str

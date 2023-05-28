import sqlite3
import datetime

connect = sqlite3.connect("firtst_sql.db")

cursor = connect.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS `timetable` (
id INTEGER NOT NULL PRIMARY KEY,
date_&_time INTEGER NOT NULL
);
""")
connect.commit()

def start():
    connect = sqlite3.connect("firtst_sql.db")
    cursor = connect.cursor()

def insert_date_lesson(*args):
    f = args[0] + '.' + args[1]
    date = datetime.datetime.strptime(f, '%d.%m.%Y.%H.%M')
    date_uts = datetime.datetime.timestamp(date)

    cursor.execute(f"""
            INSERT INTO `timetable`.`date_&_time` VALUES
                ({date_uts});
        """)
    connect.commit()
    return "Данные вставлены"


def get_date_of_all_lesson():
    res = cursor.execute("SELECT `date_&_time` FROM `timetable`;")
    lstDateTime = res.fetchall()
    str = ''

    for i in lstDateTime:
        str += f"""Занятие по изучению языка Python состоится {i[0]} в {i[1]}.\n"""
    return str

def get_date_nearest_lesson():
    pass


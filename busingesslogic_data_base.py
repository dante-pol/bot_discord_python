import sqlite3

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




def insert_date_lesson(*args):
    cursor.execute(f"""
            INSERT INTO `timetable` VALUES
                ({date}, {month}, {year});
        """)
    connect.commit()
    return "Данные вставлены"


def get_date_of_all_lesson():
    res = cursor.execute("SELECT * FROM `timetable`;")
    return res.fetchall()

def get_nearest_lesson():




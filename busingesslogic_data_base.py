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


def insert_data(data1, data2):
    cursor.execute(f"""
        INSERT INTO `timetable` VALUES
            ({data1}, {data2}, "13:30");
    """)
    connect.commit()

res = cursor.execute("SELECT * FROM `timetable`;")
print(res.fetchall())
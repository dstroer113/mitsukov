import sqlite3 as sq

with sq.connect('prokat.db') as con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS client")
    cur.execute("""CREATE TABLE IF NOT EXISTS client(
    id_client INTEGER PRIMARY KEY AUTOINCREMENT,
    fio VARCHAR,
    marka VARCHAR,
    srok INTEGER,
    summa INTEGER,
    predop FLOAT
    )""")
data_client = [
    (1, 'М.В.Аюшин', 'BMW', 32, 17005.32, 1),
    (2, '', 'Mercedes', 14, 9649.45, 0),
    (3, '', 'Porsche', 16, 14982.56, 0),
    (4, '', 'Audi', 8, 4185.67, 1),
    (5, '', 'Volkswagen', 43, 22581.99, 1),
    (6, '', 'Bentley', 4, 5201.70, )
]
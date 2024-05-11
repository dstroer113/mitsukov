import sqlite3 as sq

with sq.connect('prokat.db') as con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS car_rent")
    cur.execute(
        """CREATE TABLE IF NOT EXISTS car_rent (
        id_client INTEGER PRIMARY KEY AUTOINCREMENT,
        fio TEXT,
        brand TEXT,
        period INTEGER,
        summa FLOAT,
        prepayment BOOLEAN)
        """)

data_client = [
    (1, 'М.В.Аюшин', 'BMW', 32, 17005.32, 1),
    (2, 'Ф.С.Беров', 'Mercedes', 14, 9649.45, 0),
    (3, 'Н.Д.Беклемишев', 'Porsche', 16, 14982.56, 0),
    (4, 'А.Н.Ризаев', 'Audi', 8, 4185.67, 1),
    (5, 'К.С.Андреев', 'Volkswagen', 43, 22581.99, 1),
    (6, 'Р.О.Свистунов', 'Bentley', 4, 5201.70, 0),
    (7, 'В.Т.Невзоров', 'Dodge', 27, 13095.78, 0),
    (8, 'Т.М.Пугачев', 'Chevrolet', 66, 37893.72, 0),
    (9, 'Р.О.Обухов', 'Plymouth', 13, 29839.36, 1),
    (10, 'Л.Д.Сыркин', 'Ford', 57, 26819.34, 1)
    ]
with con:
    cur.executemany("INSERT INTO car_rent VALUES (?, ?, ?, ?, ?, ?)", data_client)
    con.commit()

with con:
    print(*cur.execute("SELECT * FROM car_rent WHERE summa > 25000.00").fetchall(), sep='\n', end='\n\n')
    print(*cur.execute("SELECT * FROM car_rent WHERE id_client = 6 OR id_client = 7").fetchall(), sep='\n', end='\n\n')
    print(*cur.execute("SELECT * FROM car_rent WHERE period BETWEEN 20 AND 50").fetchall(), sep='\n', end='\n\n')

with con:
    cur.execute('DELETE FROM car_rent WHERE brand = ?', ('Chevrolet',))
    cur.execute('DELETE FROM car_rent WHERE period > 50')
    cur.execute("DELETE FROM car_rent WHERE fio LIKE '%ин'")

with con:
    cur.execute('UPDATE car_rent SET prepayment = 1 WHERE period > 50')
    cur.execute('UPDATE car_rent SET brand = "Rolls-Royce" WHERE brand = "Ford"')
    cur.execute('UPDATE car_rent SET summa = summa * 1.2 WHERE summa < 20000.00')

with con:
    print('Измененная таблица:')
    print(*cur.execute('SELECT * FROM car_rent').fetchall(), sep='\n')

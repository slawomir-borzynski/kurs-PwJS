import sqlite3

conn = sqlite3.connect('Comments.db')
print("BD odpalona")
conn.execute('CREATE TABLE Comments(id INT PRIMARY_KEY AUTO_INCREMENT,post_id INT,name TEXT,content TEXT,inserted TIMESTAMP)')
print("Tabela utworzona")

cur=conn.cursor()
print("Generowanie przykladowych danych")
samples=[('1','1','user1','Tresc komentarza przykladowa','2019-06-27 11:13:35.951841',),
         ('2','1','user2','Nie zgadzam sie z tym artykulem, bo znam sie lepiej','2019-06-28 21:14:35.951841'),
         ('3','2','user1','Tresc komentarza przykladowa', '2019-06-28 22:15:35.951841'),
         ('4','1','user1','Niekoniecznie','2019-06-28 21:12:35.951841'),
         ('5','3','User1','Przykladowa godzina?','2019-06-28 21:12:35.951841')]
cur.executemany('INSERT INTO Comments VALUES (?,?,?,?,?)',samples)
print("Test INSERT")
print(cur.fetchall())
print("Program umiescil ",cur.rowcount," rekordow")
conn.commit()
conn.close()
print("Test udany, zamykanie BD")




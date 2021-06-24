import sqlite3

conn = sqlite3.connect('MyLittleCompany.db')
print("BD odpalona")
conn.execute('CREATE TABLE praacownicy(imie TEXT,nazwisko TEXT,nr_pracownika TEXT,adres TEXT,miasto TEXT)')
print("Tabela utworzona")

cur=conn.cursor()
print("Generowanie przykladowych danych")
samples=[('Ilona','Nazwisko1','1','ul. Przykladowa 1/69','Elblag',),
         ('Mateusz','Nazywany','2','ul. NieMielismyPomyslu 6','Dzierzgon'),
         ('Tadeusz','Kozakiwicz','3','ul. Zielonego Przyladka 23', 'Ostroda'),
         ('Marlena','Marlenowicz','4','ul. Ogolna 43/43','Elblag'),
         ('Miroslaw','PrzykladNazwy','5','ul. NieMielismyPomyslu 18','Dzierzgon')]
cur.executemany('INSERT INTO praacownicy VALUES (?,?,?,?,?)',samples)
print("Test INSERT")
print(cur.fetchall())
print("Program umiescil ",cur.rowcount," rekordow")
conn.commit()
conn.close()
print("Test udany, zamykanie BD")




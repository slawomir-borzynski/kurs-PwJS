from flask import Flask, render_template, request
import sqlite3 as sql

app = Flask(__name__)


@app.route("/")
def main():
    return render_template('glowna.html')

@app.route('/dodaj',methods = ['POST','GET'])
def dodaj():

    if request.method == 'POST':
        try:
            imie = request.form['imie']
            nazwisko = request.form['nazwisko']
            nr_pracownika = request.form['nr_pracownika']
            adres = request.form['adres']
            miasto = request.form['miasto']
            
            with sql.connect("MyLittleCompany.db") as conn:
                cur= conn.cursor()
                cur.execute("INSERT INTO praacownicy(imie,nazwisko,nr_pracownika,adres,miasto) VALUES (?,?,?,?,?)",(imie,nazwisko,nr_pracownika,adres,miasto))
                
                conn.commit();
                msg="Rekord zostal zapisany w tabeli praacownicy"
        
        
        except:
            conn.rollback()
            msg="Nie udalo sie zapisac rekordu w tabeli praacownicy. Prosze skontaktowac sie z administratorem"
        
        finally:
            return render_template('dodaj.html',msg)
            conn.close()
    


@app.route("/spojrz")
def spojrz():
    conn=sql.connect("MyLittleCompany.db")
    conn.row_factory=sql.Row
    cur=conn.cursor()
    cur.execute('SELECT * FROM praacownicy ORDER BY nazwisko')
    rekordy = cur.fetchall()
    
    return render_template('spojrz.html',rekordy=rekordy)



if __name__ == "__main__":
 app.run(debug=True,)

from flask import Flask, render_template, request,redirect,url_for,session,abort,Response
import sqlite3 as sql
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user
import datetime as time
app = Flask(__name__)

app.config['SECRET_KEY']='mojnaprawdetajemnysekert123!@#'
login_manager=LoginManager()
login_manager.init_app(app)
login_manager.login_view="login"





@app.route("/")
def main():
    return render_template('index.html')
    

@app.route("/about")
@login_required

def about_me():
    return render_template('about.html',tytul='O mnie',time=time.datetime.now().strftime("%d.%m.%Y %H:%M:%S"))

@app.route("/info")
def info():
    infos= [
        {
        'autor': {'name': 'user1'},
        'body': 'Lorem ipsum'
        },
        {
        'autor': {'name': 'user2'},
        'body': 'set dolorem'
        }
        ,
        {
        'autor': {'name': 'user3'},
        'body': 'tu na razie'
        }
        ,
        {
        'autor': {'name': 'user4'},
        'body': 'jest sciernisko'
        }]
    return render_template('info.html',tytul='Informacje',infos=infos)

@app.route("/post1")
def post1():
    tytul='post1'
    post_id=1
    comments=fetchComments(post_id)
    return render_template('post1.html',tytul=tytul,comments=comments)
@app.route("/post2")
def post2():
    tytul='post2'
    post_id=2
    comments=fetchComments(post_id)
    return render_template('post2.html',tytul=tytul,comments=comments)
@app.route("/post3")
def post3():
    tytul='post3'
    post_id=3
    comments=fetchComments(post_id)
    return render_template('post3.html',tytul=tytul,comments=comments)
@app.route("/post4")
def post4():
    tytul='post4'
    post_id=4
    comments=fetchComments(post_id)
    return render_template('post4.html',tytul=tytul,comments=comments)

class User(UserMixin):
    def __init__(self,id):
        self.id=id
        self.name="user"+str(id)
        self.password=self.name+"_secret"
    def __repr__(self):
        return "%d/%s/%s"%(self.id,self.name,self.password)

users=[User(id) for id in range (1,10)]

@app.route("/login", methods=["GET","POST"])
def login():
    tytul='Zaloguj się'
    if request.method=='POST':
        username=request.form['username']
        password=request.form['password']
        if password == username + "_secret":
            id=username.split('user')[1]
            user = User(id)
            login_user(user)
            return redirect(url_for("main"))
        else:
            return abort(401)
    else:
        return render_template('login.html', tytul=tytul)

@app.errorhandler(401)
def page_not_found(e):
    tytul="Nie moglismy wyswietlic strony"
    blad='401'
    return render_template('blad.html',tytul=tytul,blad=blad)

@app.route('/logout')
def logout():
    logout_user()
    tytul='Wylogowywanie z serwisu'
    return render_template('logout.html',tytul=tytul)

#przeladowanie usera
@login_manager.user_loader
def load_user(userid):
    return User(userid)

#komentarze?

def fetchComments(post_id):
    conn=sql.connect("Comments.db")
    conn.row_factory=sql.Row
    cur=conn.cursor()
    cur.execute('SELECT * FROM Comments WHERE post_id=? ORDER BY inserted',(post_id,))
    rekordy = cur.fetchall()
    return rekordy
@app.route('/insertComment', methods=['GET','POST'])
def insertComment():
    if request.method=='POST':
        post_id=request.form['post_id']
        name=request.form['name']
        content=request.form['tresc']
        inserted=time.datetime.now()
        with sql.connect("Comments.db") as conn:
            cursor=conn.cursor()
            cursor.execute("INSERT INTO Comments(post_id,name,content,inserted) VALUES (?,?,?,?)",(post_id,name,content,inserted))
        
        if request.form['post_id']=="1":
            return redirect(url_for("post1"))
        elif request.form['post_id']=="2":
            return redirect(url_for("post2"))
        elif request.form['post_id']=="3":
            return redirect(url_for("post3"))
        elif request.form['post_id']=="4":
            return redirect(url_for("post4"))
        


if __name__ == "__main__":

 app.run(debug=True)
 app.config=True

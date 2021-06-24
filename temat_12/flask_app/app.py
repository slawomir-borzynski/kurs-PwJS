from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def main():
    return render_template('index.html')
    

@app.route("/about")
def about_me():
    return render_template('about.html',tytul='O mnie')

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

if __name__ == "__main__":
 app.run(debug=True)

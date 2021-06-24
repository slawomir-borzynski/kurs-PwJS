from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/omnie")
def omnie():
    return render_template('omnie.html')

@app.route("/omnie2/<name>")
def about(name):
    return render_template('omnie2.html',name=name)


@app.route("/tekst")
def tekst():
    return "Pierwsza aplikacja Flask!"



if __name__ == "__main__":
 app.run(debug=True)
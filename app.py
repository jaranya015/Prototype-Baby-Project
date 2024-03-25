from flask import Flask, render_template

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/chat')
def chat():
    return render_template("chat.html")

@app.route('/setting')
def setting():
    return render_template("setting.html")

@app.route('/learn')
def learn():
    return render_template("learn.html")

if __name__ == "__main__":
    app.run(debug=True)
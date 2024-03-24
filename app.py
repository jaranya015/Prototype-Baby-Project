from flask import Flask, render_template

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return render_template("index.html")

# @app.route('/chat')
# def chat():
#     return render_template("chat.py")

# @app.route('/setting')
# def setting():
#     return render_template("setting.py")

if __name__ == "__main__":
    app.run(debug=True)
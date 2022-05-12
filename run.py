from flask import Flask
app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return "hi"

@app.route("/about")
def about():
    return "hello"

if __name__ == '__main__':
    app.run(debug=True)
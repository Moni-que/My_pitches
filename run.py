# from turtle import title
from flask import Flask, render_template,url_for
from forms import RegisterForm, LoginForm
app = Flask(__name__)


app.config['SECRET_KEY'] = '92421f0ddd14c64997f6841932943a87'

posts = [
    {
        'author':'monique',
        'title':'Blog_post_1',
        'content':'first_content',
        'date_posted':'April 1 2022'
    },
    {
        'author':'bambi',
        'title':'Blog_post_2',
        'content':'second_content',
        'date_posted':'April 1 2021'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='about')


@app.route("/register")
def register():
    form = RegisterForm
    return render_template('register.html', title='Register', form = form)

@app.route("/login")
def login():
    form = LoginForm
    return render_template('login.html', title='Login', form = form)

if __name__ == '__main__':
    app.run(debug=True)
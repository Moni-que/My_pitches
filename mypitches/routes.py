from flask import render_template,url_for, flash, redirect
from mypitches import app
from mypitches.forms import RegisterForm, LoginForm
from mypitches.models import User, Post


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


@app.route("/register", methods = ['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        flash(f'Hi,Your account has been created successfully {form.username.data}', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form = form)

@app.route("/login", methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'bambi2gmail.com' and form.password.data == 'bambii':
            flash('successfully logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful.please check your username  or pssword', 'danger')

    return render_template('login.html', title='Login', form = form)
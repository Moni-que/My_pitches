from flask import render_template,url_for, flash, redirect
from mypitches import app, db,bcrypt
from mypitches.forms import RegisterForm, LoginForm
from mypitches.models import User, Post
from flask_login import login_user, current_user,logout_user,login_required


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
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        user = User(username = form.username.data, email = form.email.data, password = hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Hi,Your account has been created successfully! You can now login', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form = form)

@app.route("/login", methods = ['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember = form.remember.data)
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful.please check your email  or pssword', 'danger')

    return render_template('login.html', title='Login', form = form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/account")
@login_required
def account():
    return render_template('account.html',title = 'Account')
# from turtle import title
from flask import Flask, render_template,url_for
app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True)
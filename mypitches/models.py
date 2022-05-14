from datetime import datetime
from mypitches import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255))
    posts = db.relationship('Post',backref = 'author',lazy = "True")

    def __repr__(self):
        return f"User('{self.username}','{self.email}', '{self.profile_pic_path}'"



class Post(db.model):
    __tablename__ = 'poosts'
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.string(100))
    date_posted = db.Column(db.DateTime, default = datetime.utcnow)
    content = db.Column(db.Text)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))

    def __repr__(self):
        return f"Post('{self.title}','{self.date_posted}'"
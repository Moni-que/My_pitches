from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)

app.config['SECRET_KEY'] = '92421f0ddd14c64997f6841932943a87'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://bambi:12345@localhost/pitches'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'



from mypitches import routes
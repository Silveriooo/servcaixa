from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'myverysecuritykey'
admin = Admin(app)

login_manager = LoginManager(app)
db = SQLAlchemy(app)

from app import routes

# descomente para criar o banco
# db.create_all()
from datetime import datetime
from app import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

@login_manager.user_loader
def get_user(user_id):
    return User.query.filter_by(id=user_id).first()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(64), index=True, unique=True, nullable=False)
    password = db.Column(db.String(30), nullable=False)
    create_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    
    def __init__(self, name, username, password):
        self.name=name
        self.username=username
        self.password = generate_password_hash(password)
        
    def verify_password(self, pwd):
        return check_password_hash(self.password, pwd)
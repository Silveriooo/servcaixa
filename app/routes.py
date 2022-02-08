from app import app, db, login_manager
from flask import render_template, redirect, request, url_for, flash
from app.models import User
from flask_login import login_user, logout_user

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/caixa')
def caixa():
    return render_template('caixa.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        username = request.form['username']
        pwd = request.form['password']
        user = User(name, username, pwd)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('home'))
    
    return render_template('register.html')

    
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        pwd = request.form['password']
        user = User.query.filter_by(username=username).first()
        if not user or not user.verify_password(pwd):
            flash("Usuário ou senha inválidos!", "danger")
            return redirect(url_for('login'))
        login_user(user)
        return redirect(url_for('home'))
             
    return render_template('login.html')

@app.route('/admin')
def admin():
    return ""

@app.route('/logout')
def logout():
    logout_user()
    flash("Usuário deslogado!", "info")
    return redirect(url_for('login'))
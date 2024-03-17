import email
from flask import Blueprint, render_template, redirect, url_for, request, flash, session
from flask_login import login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from models import db
from models import User

auth = Blueprint("auth", __name__, 
                    template_folder="./views/", 
                    static_folder='./static/', 
                    root_path="./")

@auth.route("/")
@auth.route("/login")
def login():
    return render_template("auth/login.html")

@auth.route('/logout')
def logout():
    return redirect(url_for('index'))

@auth.route('/login_post', methods=['POST'])
def login_post():
    # login code goes here
    login_info = request.form.get('login')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(username=login_info).first() or User.query.filter_by(email=login_info).first()

    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login')) # if the user doesn't exist or password is wrong, reload the page
    
    return redirect(url_for('admin.admin_index'))

@auth.route('/signup')
def signup():
    
    return render_template("auth/signup.html")

@auth.route('/signup_post', methods=['POST'])
def signup_post():
    # code to validate and add user to database goes here
    username = request.form.get("username", None)
    email = request.form.get("email", None)
    password = request.form.get("password", None)
    
    user = User.query.filter_by(email=email).first() # if this returns a user, then the email already exists in database

    # create a new user with the form data. Hash the password so the plaintext version isn't saved.
    new_user = User(email=email, username=username, password=generate_password_hash(password, method='sha256'))

    if user: # if a user is found, we want to redirect back to signup page so user can try again
        flash('Email jÃ¡ existente')
        return redirect(url_for('auth.signup'))

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login'))
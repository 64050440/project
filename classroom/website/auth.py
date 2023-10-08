# store other url path
from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return render_template("login.html", text="testing", boolean=False)


@auth.route('/logout')
def logout():
    return "<p>Logout</p>"


@auth.route('/sign-up')
def sign_out():
    return render_template("sign_up.html")

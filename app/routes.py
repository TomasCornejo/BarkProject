from app import app
from flask_login import current_user, login_user, login_required, logout_user
from app.models import User, DataRow
from app import db
from flask import abort, request
import os


@app.route('/login/<username>&<password>', methods=['GET', 'POST'])
def login(username, password):
    if current_user.is_authenticated:
        return 'Already In!!'
    user = User.query.filter_by(username=username).first()
    if user is None or user.check_password(password) or request.remote_addr != os.environ['IPADRESSADMIN']:
        return 'Not Today!!'
    login_user(user, remember=True)
    return 'Lets Get it!'


@app.route('/logout')
def logout():
    logout_user()
    return 'Go Away Man!'


@app.route('/')
def index():
    return f"Hello, Hello"


@app.route('/input&<datetime>&<value>')
@login_required
def input(datetime, value):
    if request.remote_addr == os.environ['IPADRESSADMIN']:
        row = DataRow(datetimeRegister=datetime, value=value)
        db.session.add(row)
        db.session.commit()
        return "Inserted Row: {datetime}//{value}".format(datetime=datetime, value=value)
    return abort(403)

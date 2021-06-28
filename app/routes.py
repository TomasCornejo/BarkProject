import flask

from app import app
from app.models import DataRow
from app import db, app
from flask import abort, request
import os


@app.route('/')
@app.route('/index')
def index():
    return f"Hello, Hello"


@app.route('/input', methods=['POST'])
def inputreg():
    try:
        data = request.args
        if data.get('key_input') == os.environ['INPUTKEY']:
            row = DataRow(datetimeRegister=data.get('datetime'), value=data.get('value'))
            db.session.add(row)
            db.session.commit()
            return "Inserted Row: {datetime}//{value}".format(datetime=data.get('datetime'), value=data.get('value'))
    except TypeError:
        return "Not Today"


@app.route('/showTime', methods=['GET'])
def showtime():
    try:
        json_data = flask.request.json
        if json_data['key_input'] == os.environ['INPUTKEY']:
            data = DataRow.query.all()
            return f"Data  : {data}"
    except TypeError:
        return "Not Today Yet"

import flask

from app import app
from app.models import DataRow
from app import db
from flask import abort
import os


@app.route('/')
def index():
    return f"Hello, Hello"


@app.route('/input', methods=['GET', 'POST'])
def inputreg():
    json_data = flask.request.json
    if json_data['key_input'] == os.environ['INPUTKEY']:
        row = DataRow(datetimeRegister=json_data['datetime'], value=json_data['value'])
        db.session.add(row)
        db.session.commit()
        return "Inserted Row: {datetime}//{value}".format(datetime=json_data['datetime'], value=json_data['value'])
    return abort(403)

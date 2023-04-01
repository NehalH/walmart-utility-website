from flask import Blueprint,request
from sqlalchemy.sql import text
from db import db
import datetime

vistorlog_blueprint = Blueprint('vistorlog_blueprint',__name__)

@vistorlog_blueprint.route('/add-visitors',methods=['POST'])  #  /add-visitors API
def addVisitors():
    gender = request.form['gender']
    age_group = request.form['age-group']
    comments = request.form['comments']
    currentDate = datetime.datetime.today().strftime('%Y-%m-%d')

    sql = text('INSERT INTO visitors_log (gender,age_group,comment,date) VALUES ('+gender+','+age_group+',"'+comments+'","'+currentDate+'")')
    db.engine.execute(sql)
    return "Data Logged Successfully"
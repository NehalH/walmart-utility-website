from flask import Blueprint,jsonify
from sqlalchemy.sql import text
from db import db
import datetime

dashboard_blueprint = Blueprint('dashboard_blueprint',__name__)

@dashboard_blueprint.route('/today-visitors')
def todayVisitors():

    currentDate = datetime.datetime.today().strftime('%Y-%m-%d')

    sql = text('SELECT COUNT(id) AS today_visitors FROM visitors_log WHERE date = "'+currentDate+'"')
    result = db.engine.execute(sql)
    rawdata = result.fetchall()
    jsondata = jsonify([dict(row) for row in rawdata])
    return jsondata

@dashboard_blueprint.route('/overall-visitors')
def overallVisitors():
    sql = text("SELECT COUNT(id) AS overall_visitors FROM visitors_log")
    result = db.engine.execute(sql)
    rawdata = result.fetchall()
    jsondata = jsonify([dict(row) for row in rawdata])
    return jsondata

@dashboard_blueprint.route('/male-visitors')
def maleVisitors():
    currentDate = datetime.datetime.today().strftime('%Y-%m-%d')

    sql = text('SELECT COUNT(id) AS male_visitors FROM visitors_log WHERE date = "'+currentDate+'" AND gender = 1')
    result = db.engine.execute(sql)
    rawdata = result.fetchall()
    jsondata = jsonify([dict(row) for row in rawdata])
    return jsondata


@dashboard_blueprint.route('/female-visitors')
def femaleVisitors():

    currentDate = datetime.datetime.today().strftime('%Y-%m-%d')

    sql = text('SELECT COUNT(id) AS female_visitors FROM visitors_log WHERE date = "'+currentDate+'" AND gender = 2')
    result = db.engine.execute(sql)
    rawdata = result.fetchall()
    jsondata = jsonify([dict(row) for row in rawdata])
    return jsondata
    

@dashboard_blueprint.route('/age-group-classification')
def ageGroupClassfication():

    currentDate = datetime.datetime.today().strftime('%Y-%m-%d')

    x = ''

    for a in range(1,6):

        for g in range(1,3):

            # Today's Visitors
            sqlDvisitors = text('SELECT COUNT(id) AS age_today_visitors FROM visitors_log WHERE date = "'+currentDate+'" AND gender = "'+str(g)+'" AND age_group = "'+str(a)+'"')
            resultToday = db.engine.execute(sqlDvisitors)
            associtationTodayData = resultToday.fetchall()
            ageGroupToday = associtationTodayData[0].age_today_visitors

            # Overall Visitors
            sqlOverallVisitors = text('SELECT COUNT(id) AS age_overall_visitors FROM visitors_log WHERE gender = "'+str(g)+'" AND age_group = "'+str(a)+'"')
            resultOverall = db.engine.execute(sqlOverallVisitors)
            associtationOverallData = resultOverall.fetchall()
            ageGroupOverall = associtationOverallData[0].age_overall_visitors  

            gText = ''

            if g == 1:
                gText = 'Male'
            else:
                gText = 'Female'

            if a == 1:
                ageGroup = 'Kid'
            elif a == 2:
                ageGroup = 'Teen'
            elif a == 3:
                ageGroup = 'Youngster'
            elif a == 4:
                ageGroup = 'Adult'
            elif a == 5:
                ageGroup = 'Senior Citizen'

            # Data Serialization 
            x+= '{"gender":"'+gText+'","age":"'+ageGroup+'","todayAgeClassification":"'+str(ageGroupToday)+'","overallAgeClassification":"'+str(ageGroupOverall)+'"},'
            

    x = x[:-1]
    rawjson = '['+x+']'
    return rawjson

@dashboard_blueprint.route('/bargraph')
def bargraph():

    x = ''
    for m in range(1,13):

        sql = text('SELECT COUNT(id) AS total_month_visitors FROM visitors_log WHERE Month(date) = "'+str(m)+'"')
        result = db.engine.execute(sql)
        rawdata = result.fetchall()
        totalvisitorsbymonth = rawdata[0].total_month_visitors    
        x+= '{"month":"'+str(totalvisitorsbymonth)+'"},'

    x = x[:-1]
    rawjson = '['+x+']'
    return rawjson
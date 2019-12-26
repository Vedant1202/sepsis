# import pymysql
from app import app
from db import mysql
import json
from flask import jsonify
from flask import flash, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_cors import CORS
import time
from utils.utils import not_found, create_session, calculate_age, verify_session




def report_add():
    try:
        # print(request.form.getlist())
        _status = 1
        _loc = request.form.getlist("loc")[0]
        _time = request.form.getlist("time")[0]
        _desc = request.form.getlist("info")[0]
        _skey = request.form.getlist("skey")[0]
        _uid = request.form.getlist("uid")[0]
        _mid = request.form.getlist("mid")[0]
        _date_created = int(time.time())


        # validate the received values
        if _uid and _skey and _status and _date_created and _mid and _time and _loc and _desc and verify_session(_skey, _uid) and request.method == "POST":
            # save edits
            sql = "INSERT INTO report(status, date_created, location, uid, description, mid, time) VALUES(%s, %s, %s, %s, %s, %s, %s);"
            data = (_status, _date_created, _loc, _uid, _desc, _mid, _time)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            # print(rows)
            conn.commit()
            resp = jsonify(valid=True)
            resp.status_code = 200
            # print(resp)
            return resp
        else:
            return not_found()
    except Exception as e:
        print('====================== EXCEPTION ========================')
        print(e)
    finally:
        print('Done')
        cursor.close()
        conn.close()

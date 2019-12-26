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




def report_fetch(stepsize=20):
    try:
        _skey = request.form.getlist("skey")[0]
        _uid = request.form.getlist("uid")[0]
        _start = request.form.getlist("start")[0]
        _end = int(_start) + stepsize

        # validate the received values
        if _skey and _uid and _start and _end and request.method == "POST":
            sql = "SELECT * FROM missing;"
            # data = (_uid)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql)
            rows = list(cursor.fetchall())
            conn.commit()
            resp = jsonify(data=rows[int(_start):_end])
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

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
        _pid = request.form.getlist("pid")[0]

        # validate the received values
        if _skey and _uid and _pid and verify_session(_skey, _uid) and request.method == "POST":
            sql = "SELECT * FROM patient_report WHERE pid=%s ORDER BY prid desc;"
            data = (_pid)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            rows = list(cursor.fetchall())
            conn.commit()
            resp.status_code = 200
            # print(resp)
            resp = jsonify(data=rows)
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

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
from utils.utils import not_found, create_session, calculate_age, verify_session, upload_file
from werkzeug.utils import secure_filename
import os



def report_add():
    try:
        # print(request.form.getlist())
        _title = request.form.getlist("title")[0]
        _date = request.form.getlist("date")[0]
        _pid = request.form.getlist("pid")[0]
        _skey = request.form.getlist("skey")[0]
        _uid = request.form.getlist("uid")[0]
        file = request.files.to_dict()['profImg']
        filename = secure_filename(file.filename)
        filenamefull = filename
        # filename = os.path.join('E:/HackerEarth/Missing/WebApp/backend/files/missing', filename)
        filename = 'E:/sih2020/sepsis/backend/files/patient/reports/' + filename
        print('hello')
        print(filename)

        # validate the received values
        if _uid and _skey and _date and _pid and _title and verify_session(_skey, _uid) and request.method == "POST":
            # save edits
            sql = "INSERT INTO patient_report(title, date, pid, filename, filenamefull) VALUES(%s, %s, %s, %s, %s);"
            data = (_title, _date, _pid, filenamefull, filename)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            # print(rows)
            conn.commit()
            upload_file('patient/reports')
            resp = jsonify(done=True)
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

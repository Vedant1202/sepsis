# import pymysql
from app import app
from db import mysql
import json
from flask import jsonify
from flask import flash, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_cors import CORS
import time
from utils.utils import not_found, create_session, calculate_age




def user_add(type="general"):
    try:
        _username = request.form.getlist("username")[0]
        _email = request.form.getlist("email")[0]
        _password = request.form.getlist("password")[0]
        _address = request.form.getlist("address")[0]
        _phone = int(request.form.getlist("phone")[0])
        _fname = request.form.getlist("fname")[0]
        _lname = request.form.getlist("lname")[0]
        _date = request.form.getlist("date")[0]
        _last_updated = int(time.time())
        _date_created = int(time.time())
        _age = calculate_age(time.strptime(_date, '%Y-%m-%d'))
        _type = type

        print(_password)
        # validate the received values
        if _username and _email and _password and _age and _date and _last_updated and _address and _type and _phone and _date_created and _fname and _lname and request.method == "POST":
            # do not save password as a plain text
            _hashed_password = generate_password_hash(_password)
            # save edits
            sql = "INSERT INTO user(username, email, password, last_updated, address, type, phone, date_created, fname, lname, age, bdate) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            data = (_username, _email, _hashed_password, _last_updated, _address, _type, _phone, _date_created, _fname, _lname, _age, _date)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            sql2 = "SELECT uid FROM user WHERE username=%s"
            data2 = (_username)
            cursor.execute(sql2, data2)
            rows = cursor.fetchone()
            # print(rows)
            conn.commit()
            uid = rows[0]
            skey = create_session(uid)
            resp = jsonify(uid=uid, skey=skey)
            resp.status_code = 200
            # print(resp)
            return resp
        else:
            return not_found()
    except Exception as e:
        print('====================== EXCEPTION ========================')
        print(e)
    finally:
        # print('Done')
        cursor.close()
        conn.close()

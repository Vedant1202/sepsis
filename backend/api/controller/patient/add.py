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




def user_add():
    try:
        _fname = request.form.getlist("fname")[0]
        _lname = request.form.getlist("lname")[0]
        _email = request.form.getlist("email")[0]
        _password = request.form.getlist("password")[0]
        # _dept = request.form.getlist("dept")[0]
        _dob = request.form.getlist("dob")[0]
        _gender = request.form.getlist("gender")[0]
        _phone = request.form.getlist("phone")[0]
        # _type = request.form.getlist("type")[0]
        _blood_group = request.form.getlist("blood_group")[0]
        _medical_hist = request.form.getlist("medical_hist")[0]
        _reason_of_admitants = request.form.getlist("reason_of_admitants")[0]
        _allergies = request.form.getlist("allergies")[0]
        # _last_updated = int(time.time())
        # _date_created = int(time.time())
        # _age = calculate_age(time.strptime(_date, '%Y-%m-%d'))
        # _type = type

        # validate the received values
        if _fname and _lname and _email and _password and _dob and _gender and _phone and _blood_group and _medical_hist and _reason_of_admitants and _allergies  and request.method == "POST":
            # do not save password as a plain text
            _hashed_password = generate_password_hash(_password)
            # save edits
            sql = "INSERT INTO user(fname, lname, email, password, dob, gender, phone, blood_group, medical_hist ,reason_of_admitants ,allergies , ) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            data = (_fname, _lname, _email, _hashed_password, _dob, _gender, _phone, _blood_group, _medical_hist, _reason_of_admitants, _allergies)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            print(cursor.lastrowid)
            uid = cursor.lastrowid
            conn.commit()
            # uid = rows[0]
            # skey = create_session(uid)
            resp = jsonify(uid=uid, skey='skey')
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

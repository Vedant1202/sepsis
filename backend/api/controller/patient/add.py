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
from utils.utils import not_found, create_session, calculate_age, verify_session, upload_file
from werkzeug.utils import secure_filename
import os



def patient_add():
    try:
        _fname = request.form.getlist("fname")[0]
        _lname = request.form.getlist("lname")[0]
        # _email = request.form.getlist("email")[0]
        # _password = request.form.getlist("password")[0]
        _gender = request.form.getlist("gender")[0]
        _phone = request.form.getlist("phone")[0]
        _dob = request.form.getlist("dob")[0]
        _bgroup = request.form.getlist("bgroup")[0]
        _medhist = request.form.getlist("medhist")[0]
        _roa = request.form.getlist("roa")[0]
        _allergies = request.form.getlist("allergies")[0]
        _uid = request.form.getlist("uid")[0]
        _skey = request.form.getlist("skey")[0]
        file = request.files.to_dict()['profImg']
        filename = secure_filename(file.filename)
        filenamefull = filename
        # filename = os.path.join('E:/HackerEarth/Missing/WebApp/backend/files/missing', filename)
        filename = 'E:/sih2020/sepsis/backend/files/patient/profile-pics/images/' + filename
        print('hello')
        print(filename)


        # validate the received values
        if _fname and _lname and _gender and _phone and _dob and _bgroup and _uid and _medhist and _roa and _allergies and verify_session(_skey, _uid) and request.method == "POST":
            # save edits
            sql = "INSERT INTO patient(fname, lname, gender,  phone, dob, bgroup, medhist ,roa, allergies, uid, profimg, filename) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            data = (_fname, _lname, _gender, _phone, _dob,  _bgroup, _medhist, _roa, _allergies, _uid, filename, filenamefull)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            print(cursor.lastrowid)
            uid = cursor.lastrowid
            conn.commit()
            upload_file('patient/profile-pics/images')
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
        cursor.close()
        conn.close()

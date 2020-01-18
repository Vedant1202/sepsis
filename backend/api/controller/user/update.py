# import pymysql
from db import mysql
import json
from flask import jsonify
from flask import flash, request
from werkzeug.security import generate_password_hash, check_password_hash
# from flask_cors import CORS
from utils.utils import not_found, verify_session




def user_update():
    try:
        _fname = request.form.getlist("fname")[0]
        _lname = request.form.getlist("lname")[0]
        _dept = request.form.getlist("dept")[0]
        _email = request.form.getlist("email")[0]
        # _password = request.form.getlist("password")[0]
        _type = request.form.getlist("type")[0]
        _gender = request.form.getlist("gender")[0]
        _dob = request.form.getlist("dob")[0]
        _phone = request.form.getlist("phone")[0]
        _specialization = request.form.getlist("specialization")[0]
        _experience = request.form.getlist("experience")[0]
        _registration = request.form.getlist("registration")[0]
        _uid = request.form.getlist("uid")[0]
        # _skey = request.form.getlist("skey")[0]


        # validate the received values
        if _fname and _lname  and _dept and _email and   _type and _gender and  _dob and _phone  and  _specialization and _experience and _registration and _uid  and request.method == "POST":
            # if verify_session(_skey, _uid):
                # do not save password as a plain text
                # _hashed_password = generate_password_hash(_password)
                # save edits
            sql = "UPDATE user SET fname=%s, lname=%s, dept=%s, email=%s, type=%s,  gender=%s , dob=%s ,phone=%s ,   specialization=%s , experience=%s , registration=%s WHERE uid=%s;"
            data = (_fname, _lname , _dept, _email ,  _type ,_gender, _dob,  _phone ,  _specialization, _experience , _registration, _uid)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            resp = jsonify("Success")
            resp.status_code = 200
            # else:
            #     resp = jsonify('Unauthorised')
            #     resp.status_code = 405
            print(resp)
            return resp
        else:
            return not_found()
    except Exception as e:
        print('====================== EXCEPTION ========================')
        print(e)
    finally:
        print('Done')
        # cursor.close()
        # conn.close()

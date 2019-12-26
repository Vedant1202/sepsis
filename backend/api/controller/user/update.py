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
        _name = request.form.getlist("username")[0]
        _email = request.form.getlist("email")[0]
        _password = request.form.getlist("password")[0]
        _last_updated = int(request.form.getlist("last_updated")[0])
        _address = request.form.getlist("address")[0]
        _type = request.form.getlist("type")[0]
        _phone = int(request.form.getlist("phone")[0])
        _date_created = int(request.form.getlist("date_created")[0])
        _fname = request.form.getlist("fname")[0]
        _lname = request.form.getlist("lname")[0]
        _uid = request.form.getlist("uid")[0]
        _skey = request.form.getlist("skey")[0]


        # validate the received values
        if _name and _email and _password and _skey and _last_updated and _address and _type and _phone and _date_created and _fname and _lname and request.method == "POST":
            if verify_session(_skey, _uid):
                # do not save password as a plain text
                _hashed_password = generate_password_hash(_password)
                # save edits
                sql = "UPDATE user SET username=%s, email=%s, password=%s, last_updated=%s, address=%s, type=%s, phone=%s, date_created=%s, fname=%s, lname=%s WHERE uid=%s;"
                data = (_name, _email, _hashed_password, _last_updated, _address, _type, _phone, _date_created, _fname, _lname, _uid)
                conn = mysql.connect()
                cursor = conn.cursor()
                cursor.execute(sql, data)
                conn.commit()
                resp = jsonify("Success")
                resp.status_code = 200
            else:
                resp = jsonify('Unauthorised')
                resp.status_code = 405
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

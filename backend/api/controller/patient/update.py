# import pymysql
from db import mysql
import json
from flask import jsonify
from flask import flash, request
from werkzeug.security import generate_password_hash, check_password_hash
# from flask_cors import CORS
from utils.utils import not_found, verify_session




def patient_update():
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
        # _uid = request.form.getlist("uid")[0]

        _pid = request.form.getlist("pid")[0]
        # _skey = request.form.getlist("skey")[0]


        # validate the received values
        if _fname and _lname and _gender and _phone and  _dob and _bgroup and _medhist and _roa and _allergies and _pid and request.method == "POST":
            # if verify_session(_pid):
            # do not save password as a plain text
            # _hashed_password = generate_password_hash(_password)
            # save edits
            sql = "UPDATE patient SET fname=%s, lname=%s,    gender=%s ,phone=%s , dob=%s , bgroup=%s,  medhist=%s , roa=%s , allergies=%s WHERE pid=%s;"
            data = (_fname, _lname ,_gender, _phone , _dob ,_bgroup , _medhist , _roa, _allergies, _pid)
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

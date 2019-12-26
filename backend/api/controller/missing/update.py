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
        _uid = request.form.getlist("uid")[0]
        _medications = request.form.getlist("medications")[0]
        _prescribed_by = request.form.getlist("prescribed_by")[0]
        _address = request.form.getlist("address")[0]
        _conditions = request.form.getlist("conditions")[0]
        _height = request.form.getlist("height")[0]
        _weight = request.form.getlist("weight")[0]
        _identifications = request.form.getlist("identifications")[0]
        _eye_color = request.form.getlist("eye_color")[0]
        _skin_color = request.form.getlist("skin_color")[0]
        _hair_color = request.form.getlist("hair_color")[0]
        _city = request.form.getlist("city")[0]
        _skey = request.form.getlist("skey")[0]
        _mid = request.form.getlist("mid")[0]
        _date_created = int(time.time())

        # validate the received values
        if _uid and _medications and _prescribed_by and _address and _city and _conditions and _height and _weight and _identifications and _eye_color and _skin_color and _hair_color and _date_created and _fname and _lname and verify_session(_skey, _uid) and request.method == "POST":
            # save edits
            sql = "UPDATE missing SET fname=%s, lname=%s, uid=%s, medications=%s, prescribed_by=%s, conditions=%s, height=%s, weight=%s, identifications=%s, eye_color=%s, skin_color=%s, hair_color=%s, date_created=%s, address=%s, city=%s WHERE mid=%s;"
            data = (_fname, _lname, _uid, _medications, _prescribed_by, _conditions, _height, _weight, _identifications, _eye_color, _skin_color, _hair_color, _date_created, _address, _city, _mid)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            # print(rows)
            conn.commit()
            resp = jsonify(success=True)
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
        # cursor.close()
        # conn.close()

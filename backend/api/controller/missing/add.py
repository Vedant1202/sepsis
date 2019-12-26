# import pymysql
from app import app
from db import mysql
import json
from flask import jsonify
from flask import flash, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_cors import CORS
import time
from utils.utils import not_found, create_session, calculate_age, verify_session, upload_file
from werkzeug.utils import secure_filename
import os



def missing_add():
    try:
        print(request.form.to_dict()['skey'])

        _fname = request.form.to_dict()["fname"]
        _lname = request.form.to_dict()["lname"]
        _alias = request.form.to_dict()["alias"]
        _gender = request.form.to_dict()["gender"]
        _age = request.form.to_dict()["age"]
        _address = request.form.to_dict()["address"]
        _city = request.form.to_dict()["city"]
        _nationality = request.form.to_dict()["nationality"]
        _lang = request.form.to_dict()["languages_known"]
        _height = request.form.to_dict()["height"]
        _weight = request.form.to_dict()["weight"]
        _identifications = request.form.to_dict()["identifications"]
        _eye_color = request.form.to_dict()["eye_color"]
        _skin_color = request.form.to_dict()["skin_color"]
        _hair_color = request.form.to_dict()["hair_color"]
        _conditions = request.form.to_dict()["conditions"]
        _medications = request.form.to_dict()["medications"]
        _prescribed_by = request.form.to_dict()["prescribed_by"]
        _med_hist = request.form.to_dict()["med_hist"]
        _other_med = request.form.to_dict()["other_med"]
        _fam_phone = request.form.to_dict()["fam_phone"]
        _pol_phone = request.form.to_dict()["pol_phone"]
        _pol_address = request.form.to_dict()["pol_address"]
        _skey = request.form.to_dict()["skey"]
        _uid = request.form.to_dict()["uid"]
        _date_created = int(time.time())

        file = request.files.to_dict()['profImg']
        filename = secure_filename(file.filename)
        filenamefull = filename
        # filename = os.path.join('E:/HackerEarth/Missing/WebApp/backend/files/missing', filename)
        filename = 'E:/HackerEarth/Missing/WebApp/backend/files/missing/' + filename
        print('hello')
        print(filename)

        # validate the received values
        if _uid and _skey and _fname and _date_created and _pol_phone and _pol_address and verify_session(_skey, _uid) and request.method == "POST":
            # save edits
            sql = "INSERT INTO missing(fname, lname, alias, gender, age, address, city, nationality, languages_known, height, weight, identifications, eye_color, skin_color, hair_color, conditions, medications, prescribed_by, med_hist, other_med, fam_phone, pol_phone, pol_address, uid, date_created, profimg, filename) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
            data = (_fname, _lname, _alias, _gender, _age, _address, _city, _nationality, _lang, _height, _weight, _identifications, _eye_color, _skin_color, _hair_color, _conditions, _medications, _prescribed_by, _med_hist, _other_med, _fam_phone, _pol_phone, _pol_address, _uid, _date_created, filename, filenamefull)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            upload_file('missing')
            # print(rows)
            sql2 = "SELECT mid FROM missing ORDER BY date_created DESC;"
            cursor.execute(sql2)
            row = cursor.fetchone()
            conn.commit()
            resp = jsonify(data = row, valid=True)
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

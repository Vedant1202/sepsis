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
import os




def missing_fetch_unreg(stepsize=20):
    try:
        _start = request.form.getlist("start")[0]
        _end = int(_start) + stepsize

        # validate the received values
        if _start and _end and request.method == "POST":
            sql = "SELECT mid, fname, lname, uid, medications, conditions, height, weight, identifications, date_created, city, age, gender, profImg FROM missing;"
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql)
            rows = list(cursor.fetchall())
            conn.commit()
            resp = jsonify(data=rows[int(_start):_end])
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



def missing_fetch_reg(stepsize=20):
    try:
        _skey = request.form.getlist("skey")[0]
        _uid = request.form.getlist("uid")[0]
        _start = request.form.getlist("start")[0]
        _end = int(_start) + stepsize

        # validate the received values
        if _skey and _uid and _start and _end and request.method == "POST":
            sql = "SELECT * FROM missing;"
            # data = (_uid)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql)
            # rows = cursor.fetchall()[0]
            rows = list(cursor.fetchall())
            # rows[26] = os.path.join('E:/HackerEarth/Missing/WebApp/backend/files/', rows[26])
            conn.commit()
            resp = jsonify(data=rows[int(_start):_end])
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



def missing_fetch_unreg_user():
    try:
        _mid = request.form.getlist("mid")[0]
        # _end = int(_start) + stepsize

        # validate the received values
        if _mid and request.method == "POST":
            sql = "SELECT mid, fname, lname, uid, medications, conditions, height, weight, identifications, eye_color, skin_color, hair_color, date_created, city, age, gender FROM missing WHERE mid=%s;"
            data = (_mid)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            rows = cursor.fetchone()
            conn.commit()
            resp = jsonify(data=rows)
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



def missing_fetch_reg_user():
    try:
        print(request.form.getlist('mid'))
        _skey = request.form.getlist("skey")[0]
        _uid = request.form.getlist("uid")[0]
        _mid = request.form.getlist("mid")[0]
        # _start = request.form.getlist("start")[0]
        # _end = int(_start) + stepsize

        # validate the received values
        if _skey and _uid and _mid and request.method == "POST" and verify_session(_skey, _uid):
            sql = "SELECT * FROM missing WHERE mid=%s;"
            data = (_mid)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            rows = cursor.fetchone()
            conn.commit()
            print(rows)
            resp = jsonify(data=rows)
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



def missing_fetch_search_reg(stepsize=20):
    try:
        _skey = request.form.getlist("skey")[0]
        _uid = request.form.getlist("uid")[0]
        _start = request.form.getlist("start")[0]
        _end = int(_start) + stepsize
        _keyword = request.form.getlist("keyword")[0]

        # validate the received values
        if _skey and _uid and _start and _end and _keyword and request.method == "POST" and verify_session(_skey, _uid):
            # sql = "SELECT * FROM missing WHERE fname LIKE %%s% OR lname LIKE %%s% OR medications LIKE %%s% OR prescribed_by LIKE %%s% OR conditions LIKE %%s% OR height LIKE %%s% OR weight LIKE %%s% OR eye_color LIKE %%s% OR skin_color LIKE %%s% OR hair_color LIKE %%s% OR identifications LIKE %%s% OR address LIKE %%s% OR city LIKE %%s%;"
            sql = "SELECT * FROM missing WHERE fname LIKE '%{}%' OR lname LIKE '%{}%' OR medications LIKE '%{}%' OR prescribed_by LIKE '%{}%' OR conditions LIKE '%{}%' OR height LIKE '%{}%' OR weight LIKE '%{}%' OR eye_color LIKE '%{}%' OR skin_color LIKE '%{}%' OR hair_color LIKE '%{}%' OR identifications LIKE '%{}%' OR address LIKE '%{}%' OR city LIKE '%{}%' OR age LIKE '%{}%';".format(_keyword, _keyword, _keyword, _keyword, _keyword, _keyword, _keyword, _keyword, _keyword, _keyword, _keyword, _keyword, _keyword, _keyword)
            data = (_keyword, _keyword, _keyword, _keyword, _keyword, _keyword, _keyword, _keyword, _keyword, _keyword, _keyword, _keyword, _keyword)
            # print(sql%(data))
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql)
            rows = list(cursor.fetchall())
            conn.commit()
            resp = jsonify(data=rows[int(_start):_end])
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



def missing_fetch_search_unreg(stepsize=20):
    try:
        _start = request.form.getlist("start")[0]
        _end = int(_start) + stepsize
        _keyword = request.form.getlist("keyword")[0]

        # validate the received values
        if _start and _end and _keyword and request.method == "POST":
            # sql = "SELECT * FROM missing WHERE fname LIKE %%s% OR lname LIKE %%s% OR medications LIKE %%s% OR prescribed_by LIKE %%s% OR conditions LIKE %%s% OR height LIKE %%s% OR weight LIKE %%s% OR eye_color LIKE %%s% OR skin_color LIKE %%s% OR hair_color LIKE %%s% OR identifications LIKE %%s% OR address LIKE %%s% OR city LIKE %%s%;"
            sql = "SELECT mid, fname, lname, uid, medications, conditions, height, weight, identifications, date_created, city, age, gender FROM missing WHERE fname LIKE '%{}%' OR lname LIKE '%{}%' OR medications LIKE '%{}%' OR prescribed_by LIKE '%{}%' OR conditions LIKE '%{}%' OR height LIKE '%{}%' OR weight LIKE '%{}%' OR eye_color LIKE '%{}%' OR skin_color LIKE '%{}%' OR hair_color LIKE '%{}%' OR identifications LIKE '%{}%' OR address LIKE '%{}%' OR city LIKE '%{}%' OR age LIKE '%{}%';".format(_keyword, _keyword, _keyword, _keyword, _keyword, _keyword, _keyword, _keyword, _keyword, _keyword, _keyword, _keyword, _keyword, _keyword)
            data = (_keyword, _keyword, _keyword, _keyword, _keyword, _keyword, _keyword, _keyword, _keyword, _keyword, _keyword, _keyword, _keyword)
            # print(sql%(data))
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql)
            rows = list(cursor.fetchall())
            conn.commit()
            resp = jsonify(data=rows[int(_start):_end])
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






#

# import pymysql
from app import app
from db import mysql
from flask import jsonify
from flask import request
import time
from utils.utils import not_found, verify_session




def my_patient_fetch():
    try:
        # _skey = request.form.getlist("skey")[0]
        _uid = request.form.getlist("uid")[0]

        # validate the received values
        if  _uid and request.method == "POST":
            sql = "SELECT * FROM patient WHERE uid=%s;"
            data = (_uid)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            rows = cursor.fetchall()
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


def patient_fetch():
    try:
        _uid = request.form.getlist("uid")[0]
        _skey = request.form.getlist("skey")[0]

        # validate the received values
        print(verify_session(_skey, _uid))
        if verify_session(_skey, _uid) and request.method == "POST":
            sql = "SELECT * FROM patient;"
            # data = (_uid)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql)
            rows = cursor.fetchall()
            print(rows)
            conn.commit()
            resp = jsonify(data=rows)
            # print(resp)
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



def patient_fetch_profile():
    try:
        _skey = request.form.getlist("skey")[0]
        _pid = request.form.getlist("pid")[0]

        # validate the received values
        if verify_session(_skey, _uid) and request.method == "POST":
            sql = "SELECT * FROM patient WHERE pid=%s;"
            data = (_pid)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            rows = cursor.fetchall()
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



def patient_search(stepsize=20):
    try:
        # _start = request.form.getlist("start")[0]
        _start = 0
        _end = int(_start) + stepsize
        _keyword = request.form.getlist("keyword")[0]
        print(_keyword)
        _skey = request.form.getlist("skey")[0]
        _uid = request.form.getlist("uid")[0]

        # validate the received values
        if _keyword and verify_session(_skey, _uid) and request.method == "POST":
            sql = "SELECT * FROM patient WHERE fname LIKE '%{}%' OR lname LIKE '%{}%' where uid={};".format(_keyword, _keyword, _uid)
            print(sql)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql)
            rows = list(cursor.fetchall())
            conn.commit()
            # resp = jsonify(data=rows[int(_start):_end])
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


def my_patient_search(stepsize=20):
    try:
        # _start = request.form.getlist("start")[0]
        _start = 0
        _end = int(_start) + stepsize
        _keyword = request.form.getlist("keyword")[0]
        print(_keyword)
        _skey = request.form.getlist("skey")[0]
        _uid = request.form.getlist("uid")[0]

        # validate the received values
        if _keyword and verify_session(_skey, _uid) and request.method == "POST":
            sql = "SELECT * FROM patient WHERE fname LIKE '%{}%' OR lname LIKE '%{}%' AND uid={};".format(_keyword, _keyword, _uid)
            # print(sql)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql)
            rows = list(cursor.fetchall())
            conn.commit()
            # resp = jsonify(data=rows[int(_start):_end])
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
















        #

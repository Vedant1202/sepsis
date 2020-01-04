# import pymysql
from app import app
from db import mysql
from flask import jsonify
from flask import request
import time
from utils.utils import not_found, verify_session




def patient_fetch():
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



def patient_search(stepsize=20):
    try:
        _start = request.form.getlist("start")[0]
        _end = int(_start) + stepsize
        _keyword = request.form.getlist("keyword")[0]

        # validate the received values
        if _start and _end and _keyword and request.method == "POST":
            sql = "SELECT * FROM patient WHERE fname LIKE '%{}%' OR lname LIKE '%{}%';".format(_keyword, _keyword)
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

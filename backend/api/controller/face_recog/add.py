# import pymysql
from app import app
from db import mysql
import json
from flask import jsonify
from flask import flash, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_cors import CORS
import time
from utils.utils import not_found, create_session, calculate_age, verify_session, detect_faces_in_image
import face_recognition



def encoding_add():
    try:
        # save edits
        sql = "SELECT mid, filename, profImg, fname, lname FROM missing;"
        # data = (_status, _date_created, _loc, _uid, _desc, _mid, _time)
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        # print(rows)
        matched = []
        rows = list(cursor.fetchall())
        # print(rows)
        # known_image = face_recognition.load_image_file("/home/vedant/Documents/Missing-Directory/backend/known.jpg")
        # known_image = request.files.to_dict()['profImg']
        known_image = face_recognition.load_image_file(request.files.to_dict()['profImg'])
        # known_image = face_recognition.load_image_file()
        biden_encoding = face_recognition.face_encodings(known_image)[0]
        for i in rows:
            print(i)
            filename = '/home/vedant/Documents/Missing-Directory/backend/files/missing/' + i[1]
            val = detect_faces_in_image(filename, biden_encoding)
            if val['match']:
                matched.append(i)

        # print(matched)
        conn.commit()
        resp = jsonify(matched=matched)
        resp.status_code = 200
        # print(resp)
        return resp
    except Exception as e:
        print('====================== EXCEPTION ========================')
        print(e)
    finally:
        print('Done')
        cursor.close()
        conn.close()


    # filename = '/home/vedant/Documents/Missing-Directory/backend/files/missing'
    #
    # known_image = face_recognition.load_image_file("known.jpg")
    # unknown_image = face_recognition.load_image_file("unknown.jpg")
    #
    # biden_encoding = face_recognition.face_encodings(known_image)[0]
    # unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
    #
    # results = face_recognition.compare_faces([biden_encoding], unknown_encoding)
    # print(results[0])
    # print(type(results[0]))


# encoding_add('hi');

    #

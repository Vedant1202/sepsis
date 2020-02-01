from flask import jsonify
from app import app
from db import mysql
import json
from flask import jsonify
from flask import flash, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_cors import CORS
from datetime import date
import uuid
# import face_recognition

import os
from flask import Flask, request, redirect, url_for
from werkzeug.utils import secure_filename


def not_found(error=None):
    message = {"status": 404, "message": "Not Found: " + request.url}
    resp = jsonify(message)
    resp.status_code = 404
    return resp


def check_session(uid):
    """
        Function to check if the user sessions exists or is it a
        first time login. If session exists beforehand it returns
        True, else returns False.
    """
    try:
        sql = "SELECT * FROM session WHERE uid=%s;"
        data = (uid)
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql, data)
        rows = cursor.fetchall()
        conn.commit()
        # print(len(rows))
        if rows:
            return dict(exists=True,
                        skey=rows[0][1])
        else:
            return dict(exists=False,
                        skey='')
    except Exception as e:
        print('====================== EXCEPTION ========================')
        print(e)
    finally:
        # print('Done checking')
        cursor.close()
        conn.close()


def create_session(uid):
    """
        Function to generate a universally unique id to be used as
        a session key. After inserting a new record in the session
        table, this function returns the session key
    """
    try:
        skey = uuid.uuid4().hex + uuid.uuid4().hex
        sql = "INSERT INTO session(skey, uid, status) VALUES (%s, %s, %s);"
        data = (skey, uid, 1)
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql, data)
        conn.commit()
        return skey
    except Exception as e:
        print('====================== EXCEPTION ========================')
        print(e)
    finally:
        cursor.close()
        conn.close()



def verify_session(skey, uid):
    """
        Function to verify if the session is valid. Returns true if
        session exists and is valid (ie, the status is set to '1',
        indicating that the user has an active online session), else
        returns false.
    """
    try:
        sql = "SELECT * FROM session WHERE uid=%s AND skey=%s;"
        data = (uid, skey)
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql, data)
        rows = cursor.fetchall()
        # print(rows)
        # print(rows[0][2])
        conn.commit()
        # print(len(rows))
        if rows:
            if rows[0][2] == 1:
                return True
            else:
                return False
        else:
            return False
    except Exception as e:
        print('====================== EXCEPTION ========================')
        print(e)
    finally:
        # print('Done')
        cursor.close()
        conn.close()


def update_session(uid):
    """
        Function to update session to online ie, 1.
    """
    try:
        sql = "UPDATE session SET status=1 WHERE uid=%s"
        data = (uid)
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql, data)
        rows = cursor.fetchall()
        conn.commit()
    except Exception as e:
        print('====================== EXCEPTION ========================')
        print(e)
    finally:
        # print('Done')
        cursor.close()
        conn.close()



def calculate_age(born):
    """
        Function to calculate the age using birthdate. Accepts a time.strptime()
        tuple date object as its argument. Returns the age as an integer
        (in years).
    """
    today = date.today()
    return today.year - born.tm_year - ((today.month, today.day) < (born.tm_mon, born.tm_mday))




UPLOAD_FOLDER = 'E:/sih2020/sepsis/backend/files/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'pdf', 'docx', 'doc'])

# app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



def upload_file(extFolder):
    if request.method == 'POST':
        # check if the post request has the file part
        file = request.files.to_dict()['profImg']
        # # if user does not select file, browser also
        # # submit a empty part without filename

        if file:
            if file.filename == '':
                filename = 'user-default.png' ## Use default placeholder file
            else:
                filename = secure_filename(file.filename)

            file.save(os.path.join(app.config['UPLOAD_FOLDER'], extFolder, filename))
            return redirect(request.url)

        else:
            print('none file')



def detect_faces_in_image(file_stream, known_face_encoding):
    # Pre-calculated face encoding of Obama generated with face_recognition.face_encodings(img)
    # known_face_encoding = [-0.09634063,  0.12095481, -0.00436332, -0.07643753,  0.0080383,
    #                         0.01902981, -0.07184699, -0.09383309,  0.18518871, -0.09588896,
    #                         0.23951106,  0.0986533 , -0.22114635, -0.1363683 ,  0.04405268,
    #                         0.11574756, -0.19899382, -0.09597053, -0.11969153, -0.12277931,
    #                         0.03416885, -0.00267565,  0.09203379,  0.04713435, -0.12731361,
    #                        -0.35371891, -0.0503444 , -0.17841317, -0.00310897, -0.09844551,
    #                        -0.06910533, -0.00503746, -0.18466514, -0.09851682,  0.02903969,
    #                        -0.02174894,  0.02261871,  0.0032102 ,  0.20312519,  0.02999607,
    #                        -0.11646006,  0.09432904,  0.02774341,  0.22102901,  0.26725179,
    #                         0.06896867, -0.00490024, -0.09441824,  0.11115381, -0.22592428,
    #                         0.06230862,  0.16559327,  0.06232892,  0.03458837,  0.09459756,
    #                        -0.18777156,  0.00654241,  0.08582542, -0.13578284,  0.0150229 ,
    #                         0.00670836, -0.08195844, -0.04346499,  0.03347827,  0.20310158,
    #                         0.09987706, -0.12370517, -0.06683611,  0.12704916, -0.02160804,
    #                         0.00984683,  0.00766284, -0.18980607, -0.19641446, -0.22800779,
    #                         0.09010898,  0.39178532,  0.18818057, -0.20875394,  0.03097027,
    #                        -0.21300618,  0.02532415,  0.07938635,  0.01000703, -0.07719778,
    #                        -0.12651891, -0.04318593,  0.06219772,  0.09163868,  0.05039065,
    #                        -0.04922386,  0.21839413, -0.02394437,  0.06173781,  0.0292527 ,
    #                         0.06160797, -0.15553983, -0.02440624, -0.17509389, -0.0630486 ,
    #                         0.01428208, -0.03637431,  0.03971229,  0.13983178, -0.23006812,
    #                         0.04999552,  0.0108454 , -0.03970895,  0.02501768,  0.08157793,
    #                        -0.03224047, -0.04502571,  0.0556995 , -0.24374914,  0.25514284,
    #                         0.24795187,  0.04060191,  0.17597422,  0.07966681,  0.01920104,
    #                        -0.01194376, -0.02300822, -0.17204897, -0.0596558 ,  0.05307484,
    #                         0.07417042,  0.07126575,  0.00209804]

    # Load the uploaded image file
    img = face_recognition.load_image_file(file_stream)
    # Get face encodings for any faces in the uploaded image
    unknown_face_encodings = face_recognition.face_encodings(img)

    face_found = False
    # is_obama = False

    if len(unknown_face_encodings) > 0:
        face_found = True
        # See if the first face in the uploaded image matches the known face of Obama
        match_results = face_recognition.compare_faces([known_face_encoding], unknown_face_encodings[0])
        if match_results[0]:
            return {
                'face_found': face_found,
                'match': True
            }
        else:
            return {
                'face_found': face_found,
                'match': False
            }
    else:
        return {
            'face_found': False,
            'match': False
        }





#

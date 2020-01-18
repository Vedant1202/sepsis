import pymysql
from db import mysql
from flask import jsonify
from flask import request
from werkzeug.security import check_password_hash
from utils.utils import check_session, create_session, verify_session, not_found, update_session


def login():
    try:
        _username = request.form.getlist("username")[0]
        _password = request.form.getlist("password")[0]

        if _username and _password and request.method == "POST":
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute("SELECT * FROM user WHERE BINARY email=%s", (_username))
            row = cursor.fetchone()

            if row:
                if check_password_hash(row["password"], _password):
                    sess = check_session(row["uid"])
                    update_session(row['uid'])
                    print('sess', sess)
                    print('skey=', sess['skey'])
                    print("verify_session=", verify_session(sess['skey'], row['uid']))
                    if sess['exists']:
                        resp = jsonify(uid=row["uid"],
                                       skey=sess['skey'],
                                       type=row['type'],
                                       valid=True)
                    else:
                        skey = create_session(row["uid"])
                        resp = jsonify(uid=row["uid"],
                                       skey=sess['skey'],
                                       type=row['type'],
                                       valid=True)

                else:
                    resp = jsonify(valid=False)
                resp.status_code = 200
                return resp
            else:
                resp = jsonify(valid=False)
                resp.status_code = 200
                return resp
        else:
            return not_found()
    except Exception as e:
        print('====================== EXCEPTION ========================')
        print(e)
    finally:
        cursor.close()
        conn.close()

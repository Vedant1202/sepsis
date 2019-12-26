import pymysql
from db import mysql
from flask import jsonify
from flask import request
from werkzeug.security import check_password_hash
from utils.utils import check_session, create_session, verify_session, not_found, update_session


def logout():
    try:
        _skey = request.form.getlist("skey")[0]
        _uid = request.form.getlist("uid")[0]

        if _skey and _uid and request.method == "POST" and verify_session(_skey, _uid):
            print(_uid)
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute("UPDATE session SET status=0 WHERE uid=%s", (_uid))
            conn.commit()
            resp = jsonify(logout=True)
            resp.status_code = 200
            return resp
        else:
            return not_found()
    except Exception as e:
        print('====================== EXCEPTION ========================')
        print(e)
    finally:
        print('done')
        cursor.close()
        conn.close()

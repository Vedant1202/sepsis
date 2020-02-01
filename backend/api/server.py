# import pymysql
from app import app
from db import mysql
import json
from flask import jsonify
from flask import flash, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_cors import CORS
from time import gmtime, strftime
import datetime
import uuid
# import face_recognition
# from utils import getLocalTime

from controller.authenticate.login import login
from controller.authenticate.logout import logout
from controller.user.add import user_add
from controller.patient.add import patient_add
from controller.user.update import user_update
from controller.patient.update import patient_update
from controller.user.fetch import user_fetch
from controller.patient.fetch import patient_fetch, patient_search, patient_fetch_profile, my_patient_fetch, my_patient_search
from controller.missing.fetch import missing_fetch_reg, missing_fetch_unreg, missing_fetch_reg_user, missing_fetch_unreg_user, missing_fetch_search_reg, missing_fetch_search_unreg
from controller.missing.add import missing_add
from controller.report.add import report_add
from controller.predictor.predictor import get_graph, getPredictions, get_dataframe
# from utils.utils import upload_file

# from controller.face_recog.add import encoding_add

CORS(app)


import os
from flask import Flask, request, redirect, url_for
from werkzeug.utils import secure_filename


###############################################################################
##                                ROUTES
###############################################################################


# user add route
@app.route("/user/add", methods=["POST"])
# @cross_origin()
def add_user():
    return user_add()


# user edit route
@app.route("/user/update", methods=["POST"])
# @cross_origin()
def update_user():
    return user_update()

@app.route("/patient/update", methods=["POST"])
# @cross_origin()
def update_patient():
    return patient_update()

# user edit route
@app.route("/user/fetch", methods=["POST"])
# @cross_origin()
def fetch_user():
    return user_fetch()

# user edit route
@app.route("/prediction", methods=["POST"])
# @cross_origin()
def predictions():
    return get_graph()

# user edit route
@app.route("/dataframe", methods=["POST"])
# @cross_origin()
def dataframe():
    return get_dataframe()


# patient add route
@app.route("/patient/add", methods=["POST"])
# @cross_origin()
def add_patient():
    return patient_add()


# # login route
@app.route("/login", methods=["POST"])
# # @cross_origin()
def login_user():
    return login()


# # logout route
@app.route("/logout", methods=["POST"])
# # @cross_origin()
def logout_user():
    return logout()

# # patient fetch route
@app.route("/patient/my/fetch", methods=["POST"])
# # @cross_origin()
def my_fetch_patient():
    return my_patient_fetch()

# # patient fetch route
@app.route("/patient/fetch", methods=["POST"])
# # @cross_origin()
def fetch_patient():
    return patient_fetch()

# # patient fetch route
@app.route("/patient/fetch/profile", methods=["POST"])
# # @cross_origin()
def fetch_patient_profile():
    return patient_fetch_profile()

# # patient fetch route
@app.route("/patient/search", methods=["POST"])
# # @cross_origin()
def search_patient():
    return patient_search()

# # patient fetch route
@app.route("/patient/my/search", methods=["POST"])
# # @cross_origin()
def my_search_patient():
    return my_patient_search()

# # missing profiles fetch route
@app.route("/missing/fetch/reg", methods=["POST"])
# # @cross_origin()
def fetch_missing_reg():
    return missing_fetch_reg()


# # missing profiles fetch route
@app.route("/missing/fetch/unreg", methods=["POST"])
# # @cross_origin()
def fetch_missing_unreg():
    return missing_fetch_unreg()


# # missing profiles fetch route
@app.route("/missing/fetch/profile/reg", methods=["POST"])
# # @cross_origin()
def fetch_missing_reg_user():
    return missing_fetch_reg_user()


# # missing profiles fetch route
@app.route("/missing/fetch/profile/unreg", methods=["POST"])
# # @cross_origin()
def fetch_missing_unreg_user():
    return missing_fetch_unreg_user()


# # missing profiles fetch route
@app.route("/missing/search/reg", methods=["POST"])
# # @cross_origin()
def fetch_missing_search_reg():
    return missing_fetch_search_reg()


# # missing profiles fetch route
@app.route("/missing/search/unreg", methods=["POST"])
# # @cross_origin()
def fetch_missing_search_unreg():
    return missing_fetch_search_unreg()


# # missing profiles add route
@app.route("/missing/add", methods=["POST"])
# # @cross_origin()
def add_missing():
    return missing_add()


# # missing profiles add route
@app.route("/patient/report/add", methods=["POST"])
# # @cross_origin()
def add_report():
    return report_add()



# # # missing profiles add route
# @app.route("/file", methods=["POST"])
# # # @cross_origin()
# def file_upload():
#     return upload_file()


@app.route("/face_recog", methods=["POST"])
# # @cross_origin()
def file_upload():
    return encoding_add()




# 404 handler
@app.errorhandler(404)
def not_found(error=None):
    message = {"status": 404, "message": "Not Found: " + request.url}
    resp = jsonify(message)
    resp.status_code = 404

    return resp


if __name__ == "__main__":
    # import os
    # print(os.listdir("/home/vedant/Documents/Missing-Directory/backend/files/missing/"))
    key = str(uuid.uuid4().hex + uuid.uuid4().hex)
    app.secret_key = key
    app.run()

from app import app
from flaskext.mysql import MySQL
import os

mysql = MySQL()

# MySQL configurations
app.config["MYSQL_DATABASE_USER"] = "root"
# app.config["MYSQL_DATABASE_PASSWORD"] = os.environ["MYSQL_ROOT_DB_PASSWORD"]
app.config["MYSQL_DATABASE_PASSWORD"] = 'root'
<<<<<<< HEAD
app.config["MYSQL_DATABASE_DB"] = "missing"
=======
app.config["MYSQL_DATABASE_DB"] = "sepsis"
>>>>>>> f5e817d1755102841bdaf84590d780aec04355ea
app.config["MYSQL_DATABASE_HOST"] = "localhost"
mysql.init_app(app)

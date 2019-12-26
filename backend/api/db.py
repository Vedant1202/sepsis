from app import app
from flaskext.mysql import MySQL
import os

mysql = MySQL()

# MySQL configurations
app.config["MYSQL_DATABASE_USER"] = "root"
# app.config["MYSQL_DATABASE_PASSWORD"] = os.environ["MYSQL_ROOT_DB_PASSWORD"]
app.config["MYSQL_DATABASE_PASSWORD"] = 'root'
app.config["MYSQL_DATABASE_DB"] = "sepsis"
app.config["MYSQL_DATABASE_HOST"] = "localhost"
mysql.init_app(app)

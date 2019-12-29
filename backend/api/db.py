from app import app
from flaskext.mysql import MySQL
import os

mysql = MySQL()

# MySQL configurations
app.config["MYSQL_DATABASE_USER"] = "gen"
# app.config["MYSQL_DATABASE_PASSWORD"] = os.environ["MYSQL_ROOT_DB_PASSWORD"]
app.config["MYSQL_DATABASE_PASSWORD"] = 'Sepsishack@12'
app.config["MYSQL_DATABASE_DB"] = "Sepsis"
app.config["MYSQL_DATABASE_HOST"] = "3.82.194.157"

mysql.init_app(app)
# conn = mysql.connect()

# print(conn)

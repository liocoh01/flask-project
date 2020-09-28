import connexion
import pymysql.cursors
from flask import jsonify
import flask


def connect():
    connection = pymysql.connect(host=conf.config.get('DB_HOST'),
                                 user=conf.config.get('DB_USER'),
                                 password=conf.config.get('DB_PASS'),
                                 db=conf.config.get('DB'),
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    return connection


def get_people():
    # Connect to the database
    conn = connect()
    try:
        with conn.cursor() as cursor:
            # Read a single record
            sql = "SELECT * FROM `Persons`"
            cursor.execute(sql)
            result = cursor.fetchall()
            print(result)
            return jsonify(result)
    finally:
        conn.close()


def get_by_last_name(lastname):
    # Connect to the database
    conn = connect()
    print(lastname)
    try:
        with conn.cursor() as cursor:
            # Read a single record
            sql = f"SELECT * FROM `Persons` WHERE  LastName = '{lastname}';"
            cursor.execute(sql)
            result = cursor.fetchall()
            print(result)
            return jsonify(result)
    finally:
        conn.close()


app = connexion.FlaskApp(__name__, specification_dir='swagger/')
app.add_api('swagger.yaml', arguments={'title': 'DB api'})
conf = app.app
conf.config.from_pyfile('app.conf')

from app import app
import pymysql.cursors
from flask import jsonify

@app.route('/visit')
def index():
    # Connect to the database
    app.config.from_pyfile('app.conf')
    connection = pymysql.connect(host=app.config.get('DB_HOST'),
                                 user=app.config.get('DB_USER'),
                                 password=app.config.get('DB_PASS'),
                                 db=app.config.get('DB'),
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT * FROM `Persons`"
            cursor.execute(sql)
            result = cursor.fetchall()
            print(result)
            return jsonify(result)
    finally:
        connection.close()
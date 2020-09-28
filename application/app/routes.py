import connexion
import pymysql.cursors
from flask import jsonify




def get_people():
    # Connect to the database
    connection = pymysql.connect(host=conf.config.get('DB_HOST'),
                                 user=conf.config.get('DB_USER'),
                                 password=conf.config.get('DB_PASS'),
                                 db=conf.config.get('DB'),
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

app = connexion.FlaskApp(__name__, specification_dir='swagger/')
app.add_api('swagger.yaml', arguments={'title': 'DB api'})
conf = app.app
conf.config.from_pyfile('app.conf')


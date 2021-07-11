
from flask import Flask, g
from flask_json import FlaskJSON
from os import getenv
from psycopg2 import pool
from views import main_view_endpoints_constructor

application = Flask(__name__)
FlaskJSON(application)

##Pool of connections to serve the API
application.config['postgreSQL_pool'] = pool.SimpleConnectionPool(1, 20, getenv("CONNECTIONSTRING"))

def get_connection():
    if 'conn' not in g:
        g.conn = application.config['postgreSQL_pool'].getconn()
    return g.conn

application.register_blueprint(main_view_endpoints_constructor(get_connection))

@application.teardown_appcontext
def close_conn(e):
    db = g.pop('conn', None)
    if db is not None:
        application.config['postgreSQL_pool'].putconn(db)

if __name__ == "__main__":
    application.run(port=5000, debug=True)
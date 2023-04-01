from flask import Flask #Flask Framework
from flask_cors import CORS # White List the request coming from the browser
from db import db
from visitorlog import vistorlog_blueprint
from dashboard import dashboard_blueprint

app = Flask(__name__)
CORS(app)

#Database Configuration

# Db Config
username = 'root'
password = ''
userpass = 'mysql+pymysql://' + username + ':' + password + '@'
server = '127.0.0.1'
dbname = '/wallmart_visitors'

app.config['SQLALCHEMY_DATABASE_URI'] = userpass + server + dbname
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db.init_app(app)

#register the blueprint
app.register_blueprint(vistorlog_blueprint)
app.register_blueprint(dashboard_blueprint)

@app.route('/')
def hello_world():
   return 'Hello World'

if __name__ == '__main__':
   app.debug = True
   app.run()
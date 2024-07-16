from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_httpauth import HTTPBasicAuth
from models import User, BlogPost
import resources, auth

app = Flask(__name__)
app.config.from_object('config.Config')

db = SQLAlchemy(app)
migrate = Migrate(app, db)
auth = HTTPBasicAuth()

if __name__ == '__main__':
    app.run(debug=True)
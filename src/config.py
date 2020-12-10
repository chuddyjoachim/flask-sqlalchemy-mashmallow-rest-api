from flask import Flask,redirect,url_for,render_template,request,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from dotenv import load_dotenv
import os

load_dotenv()
load_dotenv(verbose=True)

from pathlib import Path  # Python 3.6+ only
env_path = Path('..') / '.env'
load_dotenv(dotenv_path=env_path)

db_host = os.getenv("MYSQL_HOST")
db_name = os.getenv("MYSQL_NAME")
db_user = os.getenv("MYSQL_USER")
db_pass = os.getenv("MYSQL_PASSWORD")

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= f'mysql://{db_user}:@{db_host}/{db_name}'
app.config['SQLALCHEMY_TRACK_NOTIFICATIONS']= False

db = SQLAlchemy(app)
ma = Marshmallow(app)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(70))
    body = db.Column(db.String(100))

    def __init__(self,title,body):
        self.title = title
        self.body = body

# db.create_all()

class PostSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'body')

Post_schema = PostSchema()
Posts_schema = PostSchema(many = True)




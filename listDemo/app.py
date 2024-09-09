
from flask import Flask, request, render_template, redirect, session
from models import db, connect_db
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import text


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///movies_example'

app.config['SQLALCHEMY_ECHO'] = True
app.app_context().push()

db = SQLAlchemy()

connect_db(app)

app.config['SECRET_KEY'] = "junglejusticez"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

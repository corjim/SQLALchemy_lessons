from flask import Flask, request, render_template, redirect, session
# from models import db, connect_db
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///movies_example'
# specify the particular database we want the app to use......in this case movies_example is the target.
# The configuration above should come before the methods below.

app.config['SQLALCHEMY_DATABASE_URI'] = False # Helps turn up the heads notification
app.config['SQLALCHEMY_ECHO'] = True # allows to see underlying sequel codes.


db = SQLAlchemy()
app.app_context().push()

db.app = app 
# associate our db into the app
db.init_app(app)
#connect_db(app) # calling the function


# db = sqlalchemy()
# db.app = app 
# # associate our db into the app
# db.init_app(app)


app.config['SECRET_KEY'] = "junglejusticez"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

# IN THE TERMINAL RUN THE FOLLOWING COMMANDS

# ipython3
# %run app.py 
# movie = db.session.execute('SELECT * FROM movies')
# 
# list(movie) // shows the table just in a postgresql

#  The output will be a tuple, looping through will require one knowing the index of the column.

# for movie in movie:
#     print(movie[1], movie[4])
    # this prints the title and rate column in the movie table.


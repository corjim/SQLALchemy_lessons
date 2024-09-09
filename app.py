from flask import Flask
from models import db, connect_db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///movies_example'
# specify the particular database we want the app to use......in this case movies_example is the target.
# The configuration above should come before the methods below.

app.config['SQLALCHEMY_ECHO'] = True # allows to see underlying sequel codes.

app.app_context().push()

connect_db(app)

app.config['SECRET_KEY'] = "junglejusticez"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

# IN THE TERMINAL RUN THE FOLLOWING COMMANDS

# ipython3
# %run -i app.py
# from sqlalchemy import text
# from models import db
# query = text("SELECT * FROM movies")
# result = db.session.execute(query)
# [item for item in result]  - shows the result
# 
# list(movie) // shows the table just in a postgresql

#  The output will be a tuple, looping through will require one knowing the index of the column.

# for movie in movie:
#     print(movie[1], movie[4])
    # this prints the title and rate column in the movie table.


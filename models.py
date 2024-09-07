
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def connect_db(app):
    db.app = app 
    # associate our db into the app
    db.init_app(app)


    # MODELS GO BELOW
# In the terminal, run createdb pet_shop_db  (just an empty database)
# Then connect the db in postsql URI
# Then the table created below will be under the pet_shop_db in the sql. (psql ----  \c pet_shop_db)

class Pet(db.Model):
    __tablename__ = 'pets' # specify the table name

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)

    name = db.column(db.String(50),
                     nullable=True,
                     unique=True)
    species = db.Column(db.String(30), nullabe=True)

    hunger = db.Column(db.Integer, nullabe=False, default=20)


# if you do make changes in the code or table, the changes will not reflect on the file. Best practice is to Drop the table in postgresql shell, rerun the file to update the changes.



 #      USING OUR MODEL
 # 
 #   Make an instance of the method as follows:

fluffy = Pet(name ='fluffy', species = "pet") # creates a new pet called fluffy.

db.session.add(fluffy)      # required to add to database
db.session.commit()         # commit the transaction.


#       *** MULTIPLE INSERT **

# create multiple tables, add and commit one after theother.
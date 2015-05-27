from app import db
from models import BlogPost

# create database and the db tables
db.create_all()

# insert
db.session.add(BlogPost("Good", "I am good."))
db.session.add(BlogPost("Well", "I am well."))

# commit the changes
db.session.commit()
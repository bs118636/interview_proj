from . import db
from models import Post, User

# Create the database and the db tables
db.create_all()

# Insert
db.session.add(Post("Bob Marley", "Be Happy"))

# Commit
db.session.commit()
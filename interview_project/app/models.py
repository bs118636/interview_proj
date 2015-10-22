#models.py should have a Post object with the following attributes: text, author, time.

from . import db

class Post(db.Model):
	__tablename__ = 'posts'
	id = db.Column(db.Integer, primary_key=True)
	author = db.Column(db.String(20), index = True)
	comment = db.Column(db.String(300))
	timestamp = db.Column(db.DateTime)

	def __init__(self, author, comment):
		self.author = author
		self.comment = comment
		self.timestamp = datetime.utcnow()

	def __repr__(self):
		return '<Post Author %r>' % (self.author)

class User(db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(20), db.ForeignKey('posts.author'))
	email = db.Column(db.String(64))
	password = db.Column(db.String(128))

	def __init__(self, name, email, password):
		self.name = name
		self.email = email
		self.password = password

	def verify_password(self, password):
		return self.password == password


	def __repr__(self):
		return '<User %r>' % (self.name)
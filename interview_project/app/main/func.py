import re
from flask import flash

def password_validate(arg1, arg2):
	valid = True
	if len(arg1) < 6: 
		flash("Password must have at least 6 characters")
		valid = False

	if re.search("[A-Z]", arg1) == None:
		flash("Password must have an uppercase")
		valid = False

	if re.search("[a-z]", arg1) == None:
		flash("Password must have a lowercase")
		valid = False

	if re.search("[0-9@%\+\\\/!#^\?;:\.\(\)\{\}\[\]~]", arg1) == None:
		flash("Password must contain a number or special character")
		valid = False

	return valid




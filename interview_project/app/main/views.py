#views.py should have a route to specific single posts by id number.

from flask import render_template, session, redirect, url_for, current_app, flash, request
from .. import db
from . import main
from .forms import NameForm, LoginForm, RegisterForm
from ..models import Post, User
from .func import *


@main.route('/', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            return redirect(url_for('main.test'))
    return render_template('index.html', form=form)

@main.route('/Test')
def test():
    return "You are logged in"

@main.route('/Posts', methods=['GET', 'POST'])
def posts():
    comments = []
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        comment = form.comment.data
        comments.append(tuple([name, comment]))
    return render_template('posts.html', comments=comments, form=form)

@main.route('/Register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit() and password_validate(form.password.data, form.verify.data):
        user = User(email=form.email.data, 
                    name=form.username.data,
                    password=form.password.data)
        db.session.add(user)
        flash('You can now login.')
        return redirect(url_for('main.index'))
    
    return render_template('register.html', form=form)

# -*- coding: utf-8 -*-
from application import app
from flask import render_template, flash, redirect, url_for
from application.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Artem'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        },
        {
            'author': {'username': 'Ипполит'},
            'body': 'Какая гадость эта ваша заливная рыба!!'
        }
    ]
    return render_template('index.html', title='Домашняя', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Добро пожаловать, %s' % form.username.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Войти', form=form)


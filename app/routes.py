from flask import render_template, flash, redirect, url_for, request
from app import app, site_config
from app.forms import LoginForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User
from werkzeug.urls import url_parse


@app.route("/")
@login_required
def index():
    return render_template(
        'index.html',
        title='Home',
        config=site_config)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))

        login_user(user, remember=form.remember_me.data)

        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')

        return redirect(url_for(next_page))

    return render_template(
        'login.html', 
        title='login', 
        config=site_config, 
        form=form)


@app.route('/logout')
def logout():
    logout_user()

    return redirect(url_for('index'))


@app.route('/register')
def register():
    user = {'username':'Jeff'}
    return render_template(
        'index.html',
        title='register',
        config=site_config,
        user=user)


@app.route('/search')
@login_required
def search():
    user = {'username':'Jeff'}
    return render_template(
        'index.html',
        title='search',
        config=site_config,
        user=user)


@app.route('/location/<int:zipcode>')
@login_required
def location(zipcode):
    user = {'username':'Jeff'}
    return render_template(
        'index.html',
        title='location',
        config=site_config,
        user=user)


@app.route('/api/<int:zipcode>')
def api(zipcode):
    user = {'username':'Jeff'}
    return render_template(
        'index.html',
        title='api',
        config=site_config,
        user=user)


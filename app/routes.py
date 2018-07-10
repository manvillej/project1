from flask import render_template, flash, redirect, url_for
from app import app, site_config
from app.forms import LoginForm


@app.route("/")
def index():
    user = {'username':'Jeff'}
    return render_template('index.html', title='Home', config=site_config, user=user)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'login requested for user {form.username.data}, remember_me={form.remember_me.data}')
        return redirect(url_for('index'))
    user = {'username':'Jeff'}
    return render_template('login.html', title='login', config=site_config, form=form, user=user)


@app.route('/logout')
def logout():
    user = {'username':'Jeff'}
    return render_template('index.html', title='logout', config=site_config, user=user)


@app.route('/register')
def register():
    user = {'username':'Jeff'}
    return render_template('index.html', title='register', config=site_config, user=user)


@app.route('/search')
def search():
    user = {'username':'Jeff'}
    return render_template('index.html', title='search', config=site_config, user=user)


@app.route('/location/<int:zipcode>')
def location(zipcode):
    user = {'username':'Jeff'}
    return render_template('index.html', title='location', config=site_config, user=user)


@app.route('/api/<int:zipcode>')
def api(zipcode):
    user = {'username':'Jeff'}
    return render_template('index.html', title='api', config=site_config, user=user)


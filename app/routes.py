from flask import render_template
from app import app, site_config


@app.route("/")
def index():
    user = {'username':'Jeff'}
    return render_template('index.html', title='Home', config=site_config, user=user)

@app.route('/login')
def login():
    user = {'username':'Jeff'}
    return render_template('index.html', title='login', config=site_config, user=user)

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

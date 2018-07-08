from flask import render_template
from app import app

brand='Manville'

@app.route("/")
def index():
    user = {'username':'Jeff'}
    return render_template('base.html', title='Home', brand=brand, user=user)

@app.route('/login')
def login():
    user = {'username':'Jeff'}
    return render_template('base.html', title='login', brand=brand, user=user)

@app.route('/logout')
def logout():
    user = {'username':'Jeff'}
    return render_template('base.html', title='logout', brand=brand, user=user)

@app.route('/register')
def register():
    user = {'username':'Jeff'}
    return render_template('base.html', title='register', brand=brand, user=user)

@app.route('/search')
def search():
    user = {'username':'Jeff'}
    return render_template('base.html', title='search', brand=brand, user=user)

@app.route('/location/<int:zipcode>')
def location(zipcode):
    user = {'username':'Jeff'}
    return render_template('base.html', title='location', brand=brand, user=user)

@app.route('/api/<int:zipcode>')
def api(zipcode):
    user = {'username':'Jeff'}
    return render_template('base.html', title='api', brand=brand, user=user)

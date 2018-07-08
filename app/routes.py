from flask import render_template
from app import app

@app.route("/")
def index():
    user = {'username':'Jeff'}
    return render_template('index.html', title='Home', user=user)

@app.route('/login')
def login():
    user = {'username':'Jeff'}
    return render_template('index.html', title='login', user=user)

@app.route('/logout')
def logout():
    user = {'username':'Jeff'}
    return render_template('index.html', title='logout', user=user)

@app.route('/register')
def register():
    user = {'username':'Jeff'}
    return render_template('index.html', title='register', user=user)

@app.route('/search')
def search():
    user = {'username':'Jeff'}
    return render_template('index.html', title='search', user=user)
s
@app.route('/location/<int:zipcode>')
def location(zipcode):
    user = {'username':'Jeff'}
    return render_template('index.html', title='location', user=user)

@app.route('/api/<int:zipcode>')
def api(zipcode):
    user = {'username':'Jeff'}
    return render_template('index.html', title='api', user=user)

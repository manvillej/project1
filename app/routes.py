from flask import render_template
from app import app
from collections import namedtuple

project_variables = ['brand', 'project_url', 'github_url', 'social_url']
SiteConfig = namedtuple('SiteConfig', " ".join(project_variables))

site_config = SiteConfig(
    brand='Manville',
    project_url='https://github.com/manvillej/project1',
    github_url='https://github.com/manvillej',
    social_url='https://twitter.com/JeffManville',
    )


@app.route("/")
def index():
    user = {'username':'Jeff'}
    return render_template('base.html', title='Home', config=site_config, user=user)

@app.route('/login')
def login():
    user = {'username':'Jeff'}
    return render_template('base.html', title='login', config=site_config, user=user)

@app.route('/logout')
def logout():
    user = {'username':'Jeff'}
    return render_template('base.html', title='logout', config=site_config, user=user)

@app.route('/register')
def register():
    user = {'username':'Jeff'}
    return render_template('base.html', title='register', config=site_config, user=user)

@app.route('/search')
def search():
    user = {'username':'Jeff'}
    return render_template('base.html', title='search', config=site_config, user=user)

@app.route('/location/<int:zipcode>')
def location(zipcode):
    user = {'username':'Jeff'}
    return render_template('base.html', title='location', config=site_config, user=user)

@app.route('/api/<int:zipcode>')
def api(zipcode):
    user = {'username':'Jeff'}
    return render_template('base.html', title='api', config=site_config, user=user)

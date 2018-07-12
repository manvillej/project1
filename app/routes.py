from flask import render_template, flash, redirect, url_for, request
from app import app, db, site_config
from app.forms import LoginForm, RegistrationForm, SearchForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, Location
from werkzeug.urls import url_parse
from datetime import datetime
import pytz


@app.route("/")
@app.route("/index")
@login_required
def index():
    return render_template(
        'index.html',
        title='Home',
        config=site_config)


@app.route('/login', methods=['GET', 'POST'])
def login():
    template = 'login.html'
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
            
        return redirect(next_page)

    return render_template(
        template, 
        title='Login', 
        config=site_config, 
        form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    form = RegistrationForm()
 
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))

    return render_template(
        'register.html',
        title='register',
        config=site_config, form=form)


@app.route('/search', methods=['GET', 'POST'])
@login_required
def search():
    form = SearchForm()
    template = 'search.html'

    if form.validate_on_submit():
        if(form.zipcode.data is "" and form.city.data is "" and form.state.data is ""):
            flash('Please fill in a field to search')
            return render_template(
                template,
                title='search',
                config=site_config,
                form=form)

        locations = search_locations(form)

        return render_template(
            template,
            title='search',
            config=site_config,
            form=form,
            locations=locations)

    return render_template(
        template,
        title='search',
        config=site_config,
        form=form)


@app.route('/location/<int:zipcode>')
@login_required
def location(zipcode):
    template = "location.html"
    location = Location.query.filter_by(zipcode=str(zipcode))
    flash(location[0])
    location_summary = get_message(location[0], "blah", 100)
    return render_template(
        template,
        title='Location',
        config=site_config,
        location_summary=location_summary)


@app.route('/api/<int:zipcode>')
def api(zipcode):
    user = {'username':'Jeff'}
    return render_template(
        'index.html',
        title='api',
        config=site_config,
        user=user)


def search_locations(form):
    filter_query = {
        "zipcode":form.zipcode.data,
        "city":form.city.data,
        "state":form.state.data,
    }

    if form.zipcode.data is "":
        filter_query.pop("zipcode")
    if form.city.data is "":
        filter_query.pop("city")
    if form.state.data is "":
        filter_query.pop("state")

    locations = Location.query.filter_by(**filter_query).limit(20)
    return locations

def get_message(location, dark_sky_data, visits):
    location_summary = f'Hello {current_user.username}! '

    location_summary = location_summary + f'Welcome to {location.city.title()}, '
    location_summary = location_summary + f'{location.state} {location.zipcode}! '
    location_summary = location_summary + f'All {location.population} of us reside here. '
    location_summary = location_summary + f'If you are looking on GPS, '
    location_summary = location_summary + f'you can find us at '
    location_summary = location_summary + f'{location.latitude}, '
    location_summary = location_summary + f'{location.longitude} '
    location_summary = location_summary + f'(Lat, Long). '

    time = get_local_time("America/New_York",1509993277)
    location_summary = location_summary + f'Currently ({time}), '
    location_summary = location_summary + get_weather('Drizzle', 100, 60.1, .83)
    location_summary = location_summary + f'{visits} other users have checked in here. '

    return location_summary

def get_weather(summary, temperature, dewPoint, humidity):
    weather = f'there is a {summary}. It is {temperature} '
    weather = weather + f'degrees out with a dew point of {dewPoint} '
    weather = weather + f'and a humidity of {100*humidity: .1f} percent. '
    return weather

    # textual weather summary (e.g. “Clear”), temperature, dew point, and humidity (as a percentage).

def get_local_time(timezone, epoch_time):
    utc_dt = datetime.utcfromtimestamp(epoch_time).replace(tzinfo=pytz.utc)
    tz = pytz.timezone(timezone)
    local_dt = utc_dt.astimezone(tz)

    return local_dt.strftime('%H:%M:%S %Z%z')
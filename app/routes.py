from flask import render_template, flash, redirect, url_for, request
from app import app, db, site_config
from app.forms import LoginForm, RegistrationForm, SearchForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, Location
from werkzeug.urls import url_parse


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
        'login.html', 
        title='login', 
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

    if form.validate_on_submit():
        if(form.zipcode.data is "" and form.city.data is "" and form.state.data is ""):
            flash('Please enter some search criteria')
            return render_template(
                'search.html',
                title='search',
                config=site_config,
                form=form)

        locations = Location.query.filter_by(zipcode=form.zipcode.data)
        flash(f'zipcode={locations[0].zipcode}, city={locations[0].city}, state={locations[0].state}')
        return render_template(
            'search.html',
            title='search',
            config=site_config,
            form=form,
            locations=locations)

    return render_template(
        'search.html',
        title='search',
        config=site_config,
        form=form)


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


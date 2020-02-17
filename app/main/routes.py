from flask import render_template, Blueprint, request, flash, redirect, url_for

from app import db
from app.main.forms import SignupForm
from app.models import User, City, Forecast

from sqlalchemy.exc import IntegrityError

bp_main = Blueprint('main', __name__)


@bp_main.route('/')
def index():
    return render_template('index.html')


@bp_main.route('/signup/', methods=['POST', 'GET'])
def signup():
    form = SignupForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        try:
            db.session.add(user)
            db.session.commit()
            flash('Registration for {} is successful'.format(form.username.data))
            return redirect(url_for('main.index'))
        except IntegrityError:
            db.session.rollback()
            flash('ERROR! Unable to register {}. Please check your details are correct and try again.'.format(
                form.username.data), 'error')
    return render_template('signup.html', form=form)


@bp_main.route('/user/', methods=['GET'])
def show_user():
    user_list = User.query.all()
    return render_template('show_user.html', users=user_list)


@bp_main.route('/search/', methods=['POST', 'GET'])
def search():
    if request.method == 'POST':
        term = request.form['search_term']
        if term == "":
            flash("Enter a city or blog content to search for")
            return redirect('/')
        results = City.query.join(Forecast).with_entities( Forecast.forecast_datetime, City.city, Forecast.forecast, Forecast.comment).filter(
            City.city.contains(term)|Forecast.forecast.contains(term)).all()
        if not results:
            flash("No results founded.")
            return redirect('/')
        return render_template('search_results.html', results=results)
    else:
        return redirect(url_for('main.index'))

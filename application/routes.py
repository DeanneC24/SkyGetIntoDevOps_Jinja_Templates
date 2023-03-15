from flask import render_template, url_for
from application import app


@app.route('/home')
def home():
    return render_template('home.html', title='Home')


@app.route('/welcome/<name>')
def welcome(name):
    return render_template('welcome.html', name=name)


@app.route('/practice')
def practice():
    return render_template('practice.html', title="Practice")


@app.route('/about')
def about_us():
    return render_template('about.html', title="About Us", stylesheet= url_for('static', filename='about_stylesheet.css'))


@app.route('/')
def index():
    return "Hello from Flask!"

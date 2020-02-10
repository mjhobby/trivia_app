from app import app
from app.forms import LoginForm
from flask import flash, redirect, render_template


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Jacob'}
    return render_template('index.html', title='Home', user=user)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember me={}'.format(
            form.username.data, form.remember_me.data
        ))
        return redirect(url_for('/index'))
    return render_template('login.html', title='Sign In', form=form)

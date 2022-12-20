from flask import Blueprint, render_template, request, flash 

auth = Blueprint('auth', __name__)

''' Need to make sure login and sign_up can handle post and get requests '''

''' 
    Get requests is when you vist a url and recieve something, POST requests is when you submit
    something to the server
'''

@auth.route('/login', methods=['GET','POST'])   # login can now accept get and post requests
def login():
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "<p>logout</p"

@auth.route('/sign-up', methods=['GET', 'POST'])    # sign_up can now accept get and post requests
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        lastName = request.form.get('lastName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email must be greater than 4 charcters.', category='error')
        elif len(firstName) < 2:
            flash('First name must be greater than 1 character', category='error')
        elif len(lastName) < 2:
            flash('Last name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.')
        else:
            # add user to database
            flash('Account created!', category='success')


    return render_template("sign_up.html")
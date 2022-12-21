"""
stores standard routes (urls) for webstie
where users can visit

"""

from flask import Blueprint, render_template
from flask_login import login_required, current_user 

views = Blueprint('views', __name__) #defines a views blueprint

@views.route('/')   # when this root is hit, def home will execute
@login_required
def home():
    return render_template("home.html", user=current_user)



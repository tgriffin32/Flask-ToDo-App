"""
stores standard routes (urls) for webstie
where users can visit

"""

from flask import Blueprint, render_template

views = Blueprint('views', __name__) #defines a views blueprint

@views.route('/')   # when this root is hit, def home will execute
def home():
    return render_template("home.html")



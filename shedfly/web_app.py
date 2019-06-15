from flask import Flask, Blueprint, render_template, url_for

bp = Blueprint('web_app', __name__)

@bp.route('/')
@bp.route("/home")
def home():
    return render_template('home.html')

from flask import render_template, Blueprint, url_for, redirect, flash, request
import server.models

routes_blueprint = Blueprint("routes", __name__)


@routes_blueprint.route("/")
def index():
    return render_template("index.html")

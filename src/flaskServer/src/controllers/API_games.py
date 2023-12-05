from flask import render_template, request, redirect, url_for

from ..app import app

@app.route("/games/donttapit", methods=["GET"])
def GET_games_dont_tap_it():
    print(request.data)
    return render_template("../vues/templates/dontTapIt.html")

@app.route("/games/snake", methods=["GET"])
def GET_games_dont_tap_it():
    print(request.data)
    return render_template("../vues/templates/snake.html")
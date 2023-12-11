from flask import render_template, request, jsonify
from models.DB import GameSession
import uuid

from app import app, db

@app.route("/donttapit", methods=["POST"])
def GET_games_dont_tap_it():
    print('test')
    data = request.json
    id = str(uuid.uuid1())
    game = data['game']

    print(data)
    
    # Put in DB
    new_gameSession = GameSession(id=id, game=game)
    db.session.add(new_gameSession)
    db.session.commit()
    
    # echoing URL
    reply = {
        'url' : 'http://127.0.0.1:5000/donttapit/' + id
    }
    return jsonify(reply)

@app.route("/donttapit/<string:id>", methods=["GET"])
def GET_games_dont_tap_it_UUID(id: str):
    try:
        db.session.query(GameSession).filter(GameSession.id == id).first().id
        return render_template('donttapit.html')
    except:
        return "YA PAS"

from flask import render_template, request, jsonify
import uuid
from datetime import datetime, timedelta 

from app import app, db
from models.DB import GameSession

@app.route("/donttapit", methods=["POST"])
def GET_games_dont_tap_it():
    data = request.json
    id = str(uuid.uuid1())

    print(data)

    # Put in DB
    new_gameSession = GameSession(id=id, 
                                  game=data['game'], 
                                  expire_date=datetime.now(),
                                  )
    db.session.add(new_gameSession)
    db.session.commit()
    
    # echoing URL
    reply = {
        'url' : 'http://127.0.0.1:5000/donttapit/' + id
    }
    return jsonify(reply)

@app.before_request
def before_request():
    if request.endpoint == '/donttapit/<string:id>':
        print('oui')

@app.route("/donttapit/<string:id>", methods=["GET"])
def GET_games_dont_tap_it_UUID(id: str):
    try:
        db.session.query(GameSession).filter(GameSession.id == id).first().id
        return render_template('donttapit.html')
    except:
        return "YA PAS"

import os
from app import app, db

class GameSession(db.Model):
    id = db.Column(db.String(100), primary_key=True)
    game = db.Column(db.String(50))

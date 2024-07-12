import os
from app import app, db

class GameSession(db.Model):
    id = db.Column(db.String(100), primary_key=True)
    game = db.Column(db.String(50))
    expire_date = db.Column(db.DateTime)
    expired = db.Column(db.Boolean)

    def __init__(self, id, game, expire_date) -> None:
        super().__init__()
        self.id = id
        self.game = game
        self.expire_date = expire_date
        self.expired = False


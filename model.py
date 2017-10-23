# Create User model
from app import app, db
class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120))
    score = db.Column(db.String(120))

    def __init__(self, username, score):
        self.username = username
        self.score = score

    def __repr__(self):
        return '[username %r]' % self.username

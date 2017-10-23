from flask import Blueprint
from flask import jsonify, request
from flask import Response
from healthboy.model import db, Player
hb = Blueprint('healthboy', __name__)

@hb.route("/score", methods=['POST'])
def coord_handler():
    data = request.form
    username = data['name']
    score = score['latitude']
    if (username is None or score is None):
            result = "Check username or score."
            response = Response(
                response=json.dumps(result),
                status=400,
                mimetype='application/json'
               )
            return response
    result = {
            'username': username,
            'score': score
        }
		check_player = Player.query.filter_by(username=username).first()
    if(check_player is None):
        player = Player(username=username, score=score)
        db.session.add(player)
        db.session.commit()
    else:
        check_player.score = score
        db.session.commit()
    response = Response(
            response=json.dumps(result),
            status=200,
            mimetype='application/json'
        )
        return response
""" Flask Main """

from flask import jsonify, make_response
from flask_jwt_extended import JWTManager
from blacklist import BLACKLIST
from api import create_app

app = create_app('config')

jwt = JWTManager(app)


# Error Messages for JWT errors
@jwt.expired_token_loader
def expired_token_callback():
    """ Error message for expired_token_loader """
    return make_response(jsonify({'message': 'Provided token has expired!'}), 401)


@jwt.invalid_token_loader
def invalid_token_callback(error):
    """ Error message for invalid_token_loader """
    return make_response(jsonify({'message': 'Provided token is invalid!'}), 401)


@jwt.unauthorized_loader
def empty_token_callback(error):
    """ Error message for unauthorized_loader """
    return make_response(jsonify({"message": "No access token provided!"}), 401)


@jwt.needs_fresh_token_loader
def requires_fresh_token_callback():
    """ Error message for needs_fresh_token_loader """
    return make_response(jsonify({"message": "Provided token is not fresh!"}), 401)


@jwt.revoked_token_loader
def revoked_token_callback():
    """ Error message for revoked_token_loader """
    return make_response(jsonify({"message": "Token has been revoked!"}), 401)


# Blacklisting tokens
@jwt.token_in_blacklist_loader
def check_token(decrypted_token):
    """ Error message for token_in_blacklist_loader """
    return decrypted_token['jti'] in BLACKLIST


if __name__ == '__main__':
    app.run(host=app.config['HOST'],
            port=app.config['PORT'],
            debug=app.config['DEBUG'])

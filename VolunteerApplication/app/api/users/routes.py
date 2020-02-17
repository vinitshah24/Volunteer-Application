""" Routes for user """

import uuid
import pymysql
from flask import request, jsonify, Blueprint, make_response
from flask_restful import Api, Resource
from flask_jwt_extended import (
    jwt_required,
    jwt_optional,
    get_jwt_identity,
    jwt_refresh_token_required,
    fresh_jwt_required,
    get_raw_jwt,
    create_access_token,
    create_refresh_token,
)
from werkzeug.security import safe_str_cmp
from api.database import mysql
import api.users.models as queries
from blacklist import BLACKLIST

mod = Blueprint('users', __name__)
api = Api(mod)


class UserActions(Resource):
    def post(self):
        """ Create a new user """
        data = request.get_json()
        public_id = str(uuid.uuid4()),
        first_name = data['first_name'],
        last_name = data['last_name'],
        email = data['email'],
        username = data['username'],
        password = data['password'],
        is_admin = False
        try:
            if first_name and last_name and email and username and password:
                data = (public_id, first_name, last_name,
                        email, username, password, is_admin,)
                conn = mysql.connect()
                cursor = conn.cursor()
                cursor.execute(queries.INSERT_TABLE, data)
                conn.commit()
                return make_response(jsonify({'message': 'User created successfully!'}), 200)
            else:
                return make_response(jsonify({'message': 'Required fields not found!'}), 401)
        except Exception as e:
            conn.rollback()
            return make_response(jsonify({'message': 'Database Exception!'}), 401)
        finally:
            cursor.close()
            conn.close()

    @jwt_required  # Will require accesss token
    def get(self):
        """ Get user details """
        public_id = get_jwt_identity()
        #public_id = 'd5127a37-45c8-4174-8d5f-ebcd913cf0b9'
        try:
            if public_id:
                conn = mysql.connect()
                cursor = conn.cursor(pymysql.cursors.DictCursor)
                cursor.execute(queries.SELECT_BY_PUBLIC_ID, public_id)
                row = cursor.fetchone()
                user_data = {}
                user_data['public_id'] = row['public_id']
                user_data['first_name'] = row['first_name']
                user_data['last_name'] = row['last_name']
                user_data['email'] = row['email']
                user_data['username'] = row['username']
                user_data['admin'] = row['is_admin']
                return make_response(jsonify({'user': user_data}), 200)
            else:
                return make_response(jsonify({'message': 'Required fields not found!'}), 401)
        except Exception as e:
            return make_response(jsonify({'message': 'Database Exception!'}), 401)
        finally:
            cursor.close()
            conn.close()

    @jwt_required  # Will require accesss token
    def put(self):
        """ Escalate user privileges to admin """
        public_id = get_jwt_identity()
        #public_id = 'd5127a37-45c8-4174-8d5f-ebcd913cf0b9'
        try:
            if public_id:
                conn = mysql.connect()
                cursor = conn.cursor()
                cursor.execute(queries.UPDATE_ADMIN_STATUS, 1)
                conn.commit()
                return make_response(jsonify({'message': 'User promoted to Admin!'}), 200)
            else:
                return make_response(jsonify({'message': 'Required fields not found!'}), 401)
        except Exception as e:
            conn.rollback()
            return make_response(jsonify({'message': 'Database Exception!'}), 401)
        finally:
            cursor.close()
            conn.close()

    @fresh_jwt_required  # Will require a fresh token
    def delete(self):
        """ Remove a user """
        public_id = get_jwt_identity()
        #public_id = 'd5127a37-45c8-4174-8d5f-ebcd913cf0b9'
        try:
            if public_id:
                conn = mysql.connect()
                cursor = conn.cursor()
                cursor.execute(queries.DELETE_BY_PUBLIC_ID, public_id)
                conn.commit()
                return make_response(jsonify({'message': 'User deleted successfully'}), 200)
            else:
                return make_response(jsonify({'message': 'Required fields not found!'}), 401)
        except Exception as e:
            conn.rollback()
            return make_response(jsonify({'message': 'Database Exception!'}), 401)
        finally:
            cursor.close()
            conn.close()


class UpdateEmail(Resource):
    @jwt_required  # Will require accesss token
    def put(self, email):
        """ Change Email """
        public_id = get_jwt_identity()
        #public_id = 'd5127a37-45c8-4174-8d5f-ebcd913cf0b9'
        try:
            if public_id and email:
                data = (public_id, email,)
                conn = mysql.connect()
                cursor = conn.cursor()
                cursor.execute(queries.UPDATE_EMAIL, data)
                conn.commit()
                return make_response(jsonify({'message': 'Email changed successfully!'}), 200)
            else:
                return make_response(jsonify({'message': 'Required fields not found!'}), 401)
        except Exception as e:
            conn.rollback()
            return make_response(jsonify({'message': 'Database Exception!'}), 401)
        finally:
            cursor.close()
            conn.close()


class UserLogin(Resource):
    def post(self):
        """ User Login """
        json_data = request.get_json()
        input_user = json_data['username']
        input_password = json_data['password']
        try:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            data = (input_user, input_password,)
            cur = cursor.execute(queries.SELECT_BY_USERNAME_PASS, data)
            result = cursor.fetchone()
            if safe_str_cmp(result['username'], input_user) and safe_str_cmp(result['password'], input_password):
                access_token = create_access_token(
                    identity=result['public_id'], fresh=True)
                refresh_token = create_refresh_token(result['public_id'])
                return make_response(jsonify({
                    'access token': access_token,
                    'refresh token': refresh_token
                }), 200)
            else:
                return make_response(jsonify({'message': 'Invalid Credentials!'}), 401)
        except Exception as e:
            return make_response(jsonify({'message': 'Database Exception!'}), 401)
        finally:
            cursor.close()
            conn.close()


class UserLogoutAccessToken(Resource):
    @jwt_required  # Will require accesss token
    def get(self):
        """ User Logout """
        # JWT ID will be blacklisted once user logout
        jti = get_raw_jwt()['jti']
        BLACKLIST.add(jti)
        return make_response(jsonify({'message': 'Logged out (Access token revoked) successfully!'}), 200)


class UserLogoutRefreshToken(Resource):
    @jwt_refresh_token_required  # Will require refresh token
    def get(self):
        jti = get_raw_jwt()['jti']
        BLACKLIST.add(jti)
        return make_response(jsonify({'message': 'Logged out (Refresh token revoked) successfully!'}), 200)


class TokenRefresh(Resource):
    @jwt_refresh_token_required  # Requires refresh token to create new access token
    def get(self):
        """ Create a new access token """
        current_user = get_jwt_identity()
        # fresh -> False means that token refresh won't work,
        # user has to sign-in using username and password [login]
        new_token = create_access_token(identity=current_user, fresh=False)
        return make_response(jsonify({'access token': new_token}), 200)
# Currently if a user refreshes the token but the access token is still valid then
# he can use both tokens and only newly created access token will be destroyed on logout
# For future, add old access token to be added to blacklist so no once can use it anymore


api.add_resource(UserActions, '/user')
api.add_resource(UpdateEmail, '/user/<email>')
api.add_resource(UserLogin, '/login')
api.add_resource(UserLogoutAccessToken, '/logout/access_token')
api.add_resource(UserLogoutRefreshToken, '/logout/refresh_token')
api.add_resource(TokenRefresh, '/refresh')

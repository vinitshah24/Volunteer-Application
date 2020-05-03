""" Routes for user """

import uuid
import pymysql
from flask import request, jsonify, Blueprint, make_response
from flask_restful import Api, Resource
from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity,
    jwt_refresh_token_required,
    fresh_jwt_required,
    get_raw_jwt,
    create_access_token,
    create_refresh_token,
)
from werkzeug.security import safe_str_cmp
from werkzeug.security import generate_password_hash, check_password_hash
from api.database import mysql
import api.users.models as queries
from blacklist import BLACKLIST

users_blueprint = Blueprint('users', __name__)
api = Api(users_blueprint)


class UserList(Resource):
    @jwt_required  # Will require accesss token
    def get(self):
        """Get the list of users"""
        public_id = get_jwt_identity()
        try:
            if public_id:
                conn = mysql.connect()
                cursor = conn.cursor(pymysql.cursors.DictCursor)
                cursor.execute(queries.SELECT_BY_PUBLIC_ID, public_id)
                row = cursor.fetchone()
                cursor.close()
                conn.close()
                is_admin = row['is_admin']
                if is_admin:
                    conn = mysql.connect()
                    cursor = conn.cursor(pymysql.cursors.DictCursor)
                    cursor.execute(queries.SELECT_ALL)
                    users = cursor.fetchall()
                    cursor.close()
                    conn.close()
                    output = []
                    for user in users:
                        user_data = {}
                        user_data['public_id'] = user['public_id']
                        user_data['first_name'] = user['first_name']
                        user_data['last_name'] = user['last_name']
                        user_data['email'] = user['email']
                        user_data['username'] = user['username']
                        user_data['admin'] = user['is_admin']
                        output.append(user_data)
                    return jsonify({'users': output})
            else:
                return make_response(jsonify({'message': 'Required fields not found!'}), 401)
        except Exception as e:
            print(e)
            return make_response(jsonify({'message': 'Database Exception!'}), 401)

        return make_response(jsonify({'message': 'Unauthorized request!'}), 401)


class UserActions(Resource):
    def post(self):
        """ Create a new user """
        data = request.get_json()
        if len(data) == 5:
            public_id = str(uuid.uuid4()),
            first_name = data['first_name'],
            last_name = data['last_name'],
            email = data['email'],
            username = data['username'],
            password = generate_password_hash(data['password']),
            is_admin = False
        else:
            return make_response(jsonify({'message': 'Required fields count not matched!'}), 401)
        try:
            if public_id and first_name and last_name and email and username and password:
                conn = mysql.connect()
                cursor = conn.cursor()
                existing_user = cursor.execute(
                    queries.SELECT_BY_USERNAME, username)
                existing_email = cursor.execute(queries.SELECT_BY_EMAIL, email)
                conn.commit()
                cursor.close()
                conn.close()
                if existing_user == 1:
                    return make_response(jsonify({'message': 'User already exists!'}), 401)
                if existing_email == 1:
                    return make_response(jsonify({'message': 'Email already exists!'}), 401)
                if existing_user == 0 and existing_email == 0:
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
            print(e)
            return make_response(jsonify({'message': 'Database Exception!'}), 401)

    @jwt_required  # Will require accesss token
    def get(self):
        """ Get user details """
        public_id = get_jwt_identity()
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


class UpdatePassword(Resource):
    @fresh_jwt_required  # Will require a fresh token
    def post(self):
        """ Update Password """
        data = request.get_json()
        if len(data) == 1:
            password = generate_password_hash(data['password'])
            public_id = get_jwt_identity()
        else:
            return make_response(jsonify({'message': 'Required fields count not matched!'}), 401)
        try:
            if password and public_id:
                data = (password, public_id,)
                conn = mysql.connect()
                cursor = conn.cursor()
                cursor.execute(queries.UPDATE_PASSWORD, data)
                conn.commit()
                return make_response(jsonify({'message': 'Password updated successfully!'}), 200)
            else:
                return make_response(jsonify({'message': 'Required fields not found!'}), 401)
        except Exception as e:
            conn.rollback()
            return make_response(jsonify({'message': 'Database Exception!'}), 401)
        finally:
            cursor.close()
            conn.close()


class UpdateName(Resource):
    @jwt_required  # Will require accesss token
    def post(self):
        """ Update First Name, Last Name """
        data = request.get_json()
        if len(data) == 2:
            first_name = data['first_name'],
            last_name = data['last_name']
            public_id = get_jwt_identity()
        else:
            return make_response(jsonify({'message': 'Required fields count not matched!'}), 401)
        try:
            if first_name and last_name and public_id:
                data = (first_name, last_name, public_id,)
                conn = mysql.connect()
                cursor = conn.cursor()
                cursor.execute(queries.UPDATE_NAME, data)
                conn.commit()
                return make_response(jsonify({'message': 'Name updated successfully!'}), 200)
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
    def put(self):
        """ Change Email """
        data = request.get_json()
        if len(data) == 1:
            email = data['email']
            public_id = get_jwt_identity()
        else:
            return make_response(jsonify({'message': 'Required fields count not matched!'}), 401)
        try:
            if email and public_id:
                data = (email, public_id,)
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
        if len(json_data) == 2:
            input_user = json_data['username']
            input_password = json_data['password']
        else:
            return make_response(jsonify({'message': 'Required fields count not matched!'}), 401)
        try:
            if input_user and input_password:
                conn = mysql.connect()
                cursor = conn.cursor(pymysql.cursors.DictCursor)
                cur = cursor.execute(queries.SELECT_BY_USERNAME, input_user)
                result = cursor.fetchone()
                if safe_str_cmp(result['username'], input_user) \
                    and check_password_hash(result['password'], input_password):
                    access_token = create_access_token(
                        identity=result['public_id'], fresh=True)
                    refresh_token = create_refresh_token(result['public_id'])
                    return make_response(jsonify({
                        'access token': access_token,
                        'refresh token': refresh_token
                    }), 200)
                else:
                    return make_response(jsonify({'message': 'Invalid Credentials!'}), 401)
            else:
                return make_response(jsonify({'message': 'Required fields not found!'}), 401)
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
        return make_response(
            jsonify({'message': 'Logged out (Access token revoked) successfully!'}), 200
            )


class UserLogoutRefreshToken(Resource):
    @jwt_refresh_token_required  # Will require refresh token
    def get(self):
        jti = get_raw_jwt()['jti']
        BLACKLIST.add(jti)
        return make_response(
            jsonify({'message': 'Logged out (Refresh token revoked) successfully!'}), 200
            )


class TokenRefresh(Resource):
    @jwt_refresh_token_required  # Requires refresh token to create new access token
    def get(self):
        """ Create a new access token """
        current_user = get_jwt_identity()
        # fresh -> False means that token refresh won't work,
        # user has to sign-in using username and password [login]
        new_token = create_access_token(identity=current_user, fresh=False)
        return make_response(jsonify({'access token': new_token}), 200)

# Get all users
api.add_resource(UserList, '/users')
# Create, get, promote, delete user
api.add_resource(UserActions, '/user')
# Update email
api.add_resource(UpdateEmail, '/user/email')
# Update first & last name
api.add_resource(UpdateName, '/user/name')
# Update password
api.add_resource(UpdatePassword, '/user/password')
# User login to get access & refresh token
api.add_resource(UserLogin, '/login')
# Logout to kill access token
api.add_resource(UserLogoutAccessToken, '/logout/access_token')
# Logout to kill refresh token
api.add_resource(UserLogoutRefreshToken, '/logout/refresh_token')
# Refresh expired token to a new access token
api.add_resource(TokenRefresh, '/refresh')

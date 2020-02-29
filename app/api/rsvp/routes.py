""" Routes for rsvp """

import pymysql
from flask import request, jsonify, Blueprint, make_response
from flask_restful import Api, Resource
from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity,
)
from api.database import mysql
import api.users.models as user_queries
import api.events.models as event_queries
import api.rsvp.models as rsvp_queries

rsvp_blueprint = Blueprint('rsvp', __name__)
api = Api(rsvp_blueprint)


class RsvpActions(Resource):
    """RSVP Actions"""
    @jwt_required  # Will require accesss token
    def put(self):
        """ Insert a user's rsvp """
        user_public_id = get_jwt_identity()
        data = request.get_json()
        if len(data) != 1:
            return make_response(jsonify({'message': 'Required fields count not matched!'}), 401)
        else:
            events_public_id = data['events_public_id']
            try:
                # check if the row already exists in DB
                if user_public_id and events_public_id:
                    query_data = (user_public_id, events_public_id, )
                    conn = mysql.connect()
                    cursor = conn.cursor(pymysql.cursors.DictCursor)
                    cursor.execute(rsvp_queries.CHECK_RECORD, query_data)
                    row = cursor.fetchone()
                    conn.commit()
                    cursor.close()
                    conn.close()
                    count = row['record_count']
                    if count == 1:
                        return make_response(jsonify({'message': 'User RSVP already exists!'}), 401)
                    else:
                        conn = mysql.connect()
                        cursor = conn.cursor()
                        insert_status = cursor.execute(
                            rsvp_queries.INSERT_RSVP, query_data)
                        conn.commit()
                        cursor.close()
                        conn.close()
                        if insert_status == 0:
                            return make_response(jsonify({'message': 'RSVP failed!'}), 401)
                        else:
                            return make_response(
                                jsonify(
                                    {'message': 'RSVP was successfully!'}), 200
                            )
                else:
                    return make_response(jsonify({'message': 'Required fields not found!'}), 401)
            except Exception as e:
                print(e)
                return make_response(jsonify({'message': 'Database Exception!'}), 401)
        return make_response(jsonify({'message': 'Unauthorized request!'}), 401)

    def get(self):
        """Get the list of user-specific RSVP's"""
        public_id = get_jwt_identity()
        try:
            if public_id:
                conn = mysql.connect()
                cursor = conn.cursor(pymysql.cursors.DictCursor)
                cursor.execute(user_queries.SELECT_BY_PUBLIC_ID, public_id)
                rows = cursor.fetchall()
                cursor.close()
                conn.close()
                events_list = []
                for event in rows:
                    event_data = {}
                    event_data['public_id'] = event['public_id']
                    event_data['name'] = event['name']
                    event_data['category'] = event['category']
                    event_data['details'] = event['details']
                    event_data['address'] = event['address']
                    event_data['county'] = event['county']
                    event_data['state'] = event['state']
                    date = event['date']
                    event_data['date'] = date.strftime("%x")
                    event_data['time'] = str(event['time'])
                    events_list.append(event_data)
                    return jsonify({'events': events_list})
            else:
                return make_response(jsonify({'message': 'Required fields not found!'}), 401)
        except Exception as e:
            print(e)
            return make_response(jsonify({'message': 'Database Exception!'}), 401)

        return make_response(jsonify({'message': 'Unauthorized request!'}), 401)


api.add_resource(RsvpActions, '/rsvp')

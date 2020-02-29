""" Routes for events """

import uuid
from datetime import datetime
import pymysql
from dateutil.parser import *
from flask import request, jsonify, Blueprint, make_response
from flask_restful import Api, Resource
from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity,
    fresh_jwt_required,
)
from werkzeug.security import safe_str_cmp
from api.database import mysql
import api.users.models as user_queries
import api.events.models as event_queries

events_blueprint = Blueprint('events', __name__)
api = Api(events_blueprint)

class EventsList(Resource):
    """EventsList"""
    @jwt_required  # Will require accesss token
    def get(self):
        """Get the list of events"""
        public_id = get_jwt_identity()
        try:
            if public_id:
                conn = mysql.connect()
                cursor = conn.cursor(pymysql.cursors.DictCursor)
                cursor.execute(user_queries.SELECT_BY_PUBLIC_ID, public_id)
                row = cursor.fetchone()
                cursor.close()
                conn.close()
                print(safe_str_cmp(public_id, row['public_id']))
                if safe_str_cmp(public_id, row['public_id']):
                    conn = mysql.connect()
                    cursor = conn.cursor(pymysql.cursors.DictCursor)
                    cursor.execute(event_queries.SELECT_EVENTS)
                    rows = cursor.fetchall()
                    print(rows)
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
                        event_data['user_public_id'] = event['user_public_id']
                        event_data['username'] = event['username']
                        event_data['first_name'] = event['first_name']
                        event_data['last_name'] = event['last_name']
                        events_list.append(event_data)
                    return jsonify({'events': events_list})
            else:
                return make_response(jsonify({'message': 'Required fields not found!'}), 401)
        except Exception as e:
            print(e)
            return make_response(jsonify({'message': 'Database Exception!'}), 401)

        return make_response(jsonify({'message': 'Unauthorized request!'}), 401)


class EventActions(Resource):
    """EventActions"""
    @jwt_required  # Will require accesss token
    def post(self):
        """ Create a new event """
        jwt_id = get_jwt_identity()
        data = request.get_json()
        if len(data) != 8:
            return make_response(jsonify({'message': 'Required fields count not matched!'}), 401)
        else:
            public_id = str(uuid.uuid4())
            name = data['name']
            category = data['category']
            details = data['details']
            address = data['address']
            county = data['county']
            state = data['state']
            date = data['date']
            time = data['time']
            user_public_id = jwt_id
            try:
                # check if the row already exists in DB
                if public_id and name and category and details and address and \
                        county and state and date and time and user_public_id:
                    data = (public_id, name, category, details, address,
                            county, state, date, time, user_public_id,)
                    conn = mysql.connect()
                    cursor = conn.cursor()
                    insert_status = cursor.execute(
                        event_queries.INSERT_EVENT, data)
                    conn.commit()
                    cursor.close()
                    conn.close()
                    if insert_status == 0:
                        return make_response(jsonify({'message': 'Event creation failed!'}), 401)
                    else:
                        return make_response(jsonify({'message': 'Event was created successfully!'}), 200)
                else:
                    return make_response(jsonify({'message': 'Required fields not found!'}), 401)
            except Exception as e:
                print(e)
                return make_response(jsonify({'message': 'Database Exception!'}), 401)
        return make_response(jsonify({'message': 'Unauthorized request!'}), 401)


    @fresh_jwt_required  # Will require a fresh token
    def delete(self):
        """Remove an event"""
        user_public_id = get_jwt_identity()
        data = request.get_json()
        events_public_id = data["events_public_id"]
        try:
            if user_public_id and events_public_id:
                input_data = (events_public_id, user_public_id,)
                conn = mysql.connect()
                cursor = conn.cursor()
                return_code = cursor.execute(event_queries.DELETE_EVENT, input_data)
                conn.commit()
                if return_code == 1:
                    return make_response(jsonify({'message': 'Event deleted successfully'}), 200)
                else:
                     return make_response(jsonify({'message': 'Event deletion failed'}), 200)
            else:
                return make_response(jsonify({'message': 'Required fields not found!'}), 401)
        except Exception as e:
            conn.rollback()
            return make_response(jsonify({'message': 'Database Exception!'}), 401)
        finally:
            cursor.close()
            conn.close()


# Get all events
api.add_resource(EventsList, '/events')
# Insert, Delete an event
api.add_resource(EventActions, '/event')

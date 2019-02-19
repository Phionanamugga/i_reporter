from flask import jsonify, request, abort, Blueprint
from .models import Incident, User
from datetime import datetime
from flask import Flask
import re
app = Flask(__name__)


name_regex = r"[a-zA-Z]"
password_regex = r"(?=.*[0-9])"
username_regex = r"[a-zA-Z0-9_]"
phone_regex = r"\d{3}-\d{3}-\d{4}"
incidents = []


@app.route('/api/v1/incidents', methods=['POST'])
def create_incident():
    # Creates a new incident
    data = request.get_json()
    incident_id = len(incidents)+1
    created_on = datetime.now()
    incident = Incident(incident_id, data['title'], data['description'],
                        data['status'], data['comments'],
                        created_on, data['location'], data['incident_type'],
                        data['images'], data['videos'], data['created_by'])
    incidents.append(incident)
    return jsonify({"message": " Successfully created"}), 201


@app.route('/api/v1/incidents', methods=['GET'])
def fetch_incidents():
    # fetches all user's incidents
    Incidents = [incident.get_incident() for incident in incidents]
    return jsonify({"incidents": Incidents}), 200


@app.route('/api/v1/incidents/<int:incident_id>', methods=['GET'])
def fetch_single_incident(incident_id):
    fetched_incident = []
    incident = incidents[incident_id - 1]
    fetched_incident.append(incident.get_incident())
    return jsonify({"incident": fetched_incident}), 200


@app.route('/api/v1/incidents/<int:incident_id>', methods=['PUT'])
def edit_incident(incident_id):
    # function for editing an incident
    if not incident_id:
        return jsonify({"message": "Invalid incident_id"}), 400
    data = request.get_json()
    for incident in incidents:
        if int(incident.incident_id) == int(incident_id):
            incident.incident_type = data['incident_type']
            incident.title = data['title']
            incident.description = data['description']
            incident.location = data['location']
            incident.status = data['status']
            incident.images = data['images']
            incident.videos = data['videos']
            incident.created_by = data['created_by']
    return jsonify({'message': "successfully edited"}), 201


@app.route('/api/v1/incidents/<int:incident_id>', methods=['DELETE'])
def delete_incident(incident_id):
    # this function enables user delete an incident
    if incident_id == 0 or incident_id > len(incidents):
        return jsonify({"message": "Index is out of range"}), 400
    for incident in incidents:
        if incident.incident_id == incident_id:
            incidents.remove(incident)
    return jsonify({"message": "incident successfully deleted"}), 201

users = [
    User(1, 'aldo', 'Okware', 'Padde', 'aldo@gmail.com', '0779862290','aldo', 'test12345'),
]

user_id_mapping = {u.user_id: u for u in users}
user_email_mapping = {u.email: u for u in users}


@app.route('/api/v1/users', methods=['POST'])
def register_user():
    global users
    # registers a  new user
    data = request.get_json()
    user_id = len(users)+1
    registered_on = datetime.now()
    username = data['username']
    text_fields = ['othernames', 'firstname', 'lastname', 'username']
    user_fields = ['othernames', 'firstname', 'lastname']
    key_fields = ['email', 'password']

    for user in users:
        print(user.email)
        print(data['email'])
        if user.email == data['email']:
            return jsonify({"message": "user already exists!"}), 400
    for name in user_fields:
        if not re.match(name_regex, data[name]):
            return jsonify({'message': 'Enter correct ' + name + ' format'}), 400
    
    for key in key_fields:
        if not data[key] or data[key].isspace():
            return jsonify({'message': key + ' field can not be empty.'}), 400   
    if not username or username.isspace():
        return jsonify({'message': 'Username can not be empty.'}), 400 
    if not re.match(r"[^@.]+@[A-Za-z]+\.[a-z]+", data['email']):
        return jsonify({'message': 'Enter a valid email address.'}), 400
    if not re.match(username_regex, data['username']):
        return jsonify({'message': 'Enter a valid username'}), 400
    if not re.match(phone_regex, data['phonenumber']):
        return jsonify({'message': 'Enter phone format 123-456-7890'}), 400
    if len(data['password']) < 8:
        return jsonify({'message': 'Password must be atleast 8 characters'}), 400  
    user = User(user_id, data['firstname'], data['lastname'],
                data['othernames'], data['email'], data['phonenumber'],
                data['username'], data['password'])
    users.append(user)
    return jsonify({"user_details": user.__dict__}), 201


@app.route('/api/v1/users', methods=['GET'])
def fetch_users():
    global users
    # fetches all user's records
    data = [user.__dict__ for user in users]
    return jsonify({"users": data})


@app.route('/api/v1/users/<int:user_id>', methods=['GET'])
# this fetches a single user account
def fetch_single_user_details(user_id):
    user = user_id_mapping.get(user_id, None)
    if user is None:
        return jsonify({"message": "user doesnot exist"}), 404
    return jsonify({"user": user.__dict__}), 200


@app.route('/api/v1/users/login', methods=['POST'])
def login():
    # this function enables user to log in  
    data = request.get_json()
    email = data.get('email')
    user = user_email_mapping.get(email, None)
    if user is None:
        return jsonify({'message': f"No user with provided email {email}"}), 404
    else:
        if user.password == data['password']:
            return jsonify({'message': 'user successfully logged in'})
        return jsonify({'message': 'incorrect password'}), 400


@app.route('/api/v1/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    # this function enables user to delete his/her account
    if user_id in users == user_id:
            users.remove(user)
    return jsonify({"message": "account successfully deleted"}), 201
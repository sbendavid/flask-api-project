from flask import request, jsonify, Blueprint
from flask_jwt_extended import create_access_token
from app import db, bcrypt
from models import User, Organisation, UserOrganisation

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    errors = validate_user_data(data)
    if errors:
        return jsonify({"errors": errors}), 422

    if User.query.filter((User.email == data['email']) | (User.userId == data['userId'])).first():
        return jsonify({"errors": [{"field": "email or userId", "message": "Email or UserId already exists"}]}), 422

    user = User(
        userId=data['userId'],  # Corrected field name
        first_name=data['firstName'],
        last_name=data['lastName'],
        email=data['email'],
        phone=data.get('phone')
    )
    user.set_password(data['password'])
    db.session.add(user)
    db.session.commit()

    organisation = Organisation(
        name=f"{user.first_name}'s Organisation"
    )
    db.session.add(organisation)
    db.session.commit()

    user_org = UserOrganisation(user_id=user.id, organisation_id=organisation.id)
    db.session.add(user_org)
    db.session.commit()

    access_token = create_access_token(identity=user.id)
    return jsonify({
        "status": "success",
        "message": "Registration successful",
        "data": {
            "accessToken": access_token,
            "user": {
                "userId": user.userId,
                "firstName": user.first_name,
                "lastName": user.last_name,
                "email": user.email,
                "phone": user.phone,
            }
        }
    }), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()
    if user and user.check_password(data['password']):
        access_token = create_access_token(identity=user.id)
        return jsonify({
            "status": "success",
            "message": "Login successful",
            "data": {
                "accessToken": access_token,
                "user": {
                    "userId": user.userId,
                    "firstName": user.first_name,
                    "lastName": user.last_name,
                    "email": user.email,
                    "phone": user.phone,
                }
            }
        }), 200
    return jsonify({"status": "Bad request", "message": "Authentication failed", "statusCode": 401}), 401

def validate_user_data(data):
    required_fields = ['userId', 'firstName', 'lastName', 'email', 'password']
    errors = []
    for field in required_fields:
        if field not in data or not data[field]:
            errors.append({"field": field, "message": f"{field} is required"})
    return errors

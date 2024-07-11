from flask import request, jsonify, Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from models import Organisation, UserOrganisation, User


organisation_bp = Blueprint('organisation_bp', __name__)

@organisation_bp.route('', methods=['POST'])
@jwt_required()
def create_organisation():
    data = request.get_json()
    if 'name' not in data or not data['name']:
        return jsonify({"status": "Bad Request", "message": "Client error", "statusCode": 400}), 400

    user_id = get_jwt_identity()
    organisation = Organisation(name=data['name'], description=data.get('description'))
    db.session.add(organisation)
    db.session.commit()

    user_org = UserOrganisation(user_id=user_id, organisation_id=organisation.id)
    db.session.add(user_org)
    db.session.commit()

    return jsonify({
        "status": "success",
        "message": "Organisation created successfully",
        "data": {
            "orgId": organisation.id,
            "name": organisation.name,
            "description": organisation.description
        }
    }), 201

@organisation_bp.route('', methods=['GET'])
@jwt_required()
def get_organisations():
    user_id = get_jwt_identity()
    organisations = Organisation.query.join(UserOrganisation).filter(UserOrganisation.user_id == user_id).all()
    return jsonify({
        "status": "success",
        "message": "Organisations fetched successfully",
        "data": {
            "organisations": [
                {
                    "orgId": org.id,
                    "name": org.name,
                    "description": org.description
                } for org in organisations
            ]
        }
    }), 200

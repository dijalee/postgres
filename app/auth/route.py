from flask import Blueprint, request, jsonify
import jwt
from datetime import datetime, timedelta
from flask_jwt_extended import create_access_token,get_jwt_identity,jwt_required
from app.lib.bd import getUserByEmail,get_role_by_email


auth_bp=Blueprint('bpAuth',__name__)

@auth_bp.route('/login',methods=['POST'])
def login():
    data = request.get_json()

    if data['email'] and data['mdp'] :
        token=create_access_token (identity=data.get('email'))       
        return jsonify({'token': token})
    else:
        return jsonify({'message': 'Invalid credentials'}), 401
    
@auth_bp.route('/me')
@jwt_required()
def info_user():
    email=get_jwt_identity()
    user=get_role_by_email(email)
    return user, 200
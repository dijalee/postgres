from flask import Blueprint, request, jsonify
auth_bp=Blueprint('auth_bp',__name__)
@auth_bp.route('/creer_prompt')
def creer_prompt():
    query="""insert into prompt"""
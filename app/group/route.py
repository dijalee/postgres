from flask import Blueprint, request, jsonify
group_bp=Blueprint('group_bp',__name__)
@group_bp.route('/creer_prompt')
def creer_prompt():
    query="""insert into prompt"""
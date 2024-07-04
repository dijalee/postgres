from flask import Blueprint, request, jsonify

prompt_bp=Blueprint('prompt_bp',__name__)
@prompt_bp.route('/creer_prompt')
def creer_prompt():
    query="""insert into prompt"""
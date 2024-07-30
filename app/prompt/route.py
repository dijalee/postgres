from flask import Blueprint, jsonify, request
from app.lib.bd import *
from flask_jwt_extended import get_jwt_identity,jwt_required,verify_jwt_in_request


prompt_bp=Blueprint('prompt_bp',__name__)

@prompt_bp.route('/all')
def liste_prompt():
    prompt=lister_prompt()
    print(prompt)
    return jsonify({'prompt': prompt})

@prompt_bp.route('/add',methods=['POST'])
@jwt_required()
def add_prompt():
    email=get_jwt_identity()
    user=getUserByEmail(email)
    if user.get('role')=='user':
        data = request.get_json() 
        titre = data.get('titre')
        texte = data.get('texte')
        statut = data.get('statut')
        prix = data.get('prix')
        ajout_prompt(titre,texte,statut,prix)
        conn.commit
        return('prompt cree avec succes')
    else:
            return jsonify({'message':'Vous n\'avez pas les droits pour effectuer cette action'})

@prompt_bp.route('/del')
@jwt_required()
def del_prompt():
    email=get_jwt_identity()
    user=getUserByEmail(email)
    if user.get('role')=='admin':
        data=request.get_json()
        id = data.get('id')
        supprimer_Prompt(id)
    conn.commit
    print('prompt supprimer avec success')
    
@prompt_bp.route('/modification')
@jwt_required()
def update_prompt():
    data=request.get_json()
    id = data.get('id_prompt')
    titre = data.get('titre')
    desc = data.get('description')
    statut = data.get('statut')
    modification_prompt(titre,desc,statut,id)
    conn.commit()
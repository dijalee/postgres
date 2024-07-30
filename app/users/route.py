from flask import Blueprint, request, jsonify
from app.lib.bd import *
from flask_jwt_extended import jwt_required


bpUser=Blueprint('bpUser',__name__)
@bpUser.route('/lister_user',methods=['GET'])
@jwt_required()
def list_user():
    query = "select * from utilisateur"
    cur.execute(query)
    list=cur.fetchall()
    return jsonify(list)

@bpUser.route('/new', methods=['POST'])
@jwt_required()
def create_user():
    data = request.get_json()
    try:  
        nom = data.get('nom_user')
        prenom = data.get('prenom')
        email = data.get('email')
        mdp = data.get('mdp')
        role = data.get('role')

        inserer_utilisateur(nom, prenom, email, mdp,role)  # Appeler la fonction d'insertion de l'utilisateur
        conn.commit()  # Valider les modifications dans la base de données
        return jsonify({'message': 'Utilisateur créé avec succès'})  
    except Exception as error:
        print("Erreur lors de la création de l'utilisateur", error)
        conn.rollback()  # Annuler en cas d'erreur
        return jsonify({"message': 'Erreur lors de la création de l'utilisateur"}), 500 


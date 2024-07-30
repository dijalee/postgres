from flask import Blueprint, request, jsonify
from app.lib.bd import *

group_bp=Blueprint('group_bp',__name__)
@group_bp.route('/lister_group',methods=['GET'])
def list_group():
    query = "select * from groupe"
    cur.execute(query)
    list=cur.fetchall()
    print(list)
    return jsonify(list)

@group_bp.route('/new', methods=['POST'])
def create_group():
    data = request.get_json()
    nom = data.get('nom')

    try:  

        inserer_groupe(nom)  # Appeler la fonction d'insertion de groupe
        conn.commit()  # Valider les modifications dans la base de données
        return jsonify({'message': 'groupe créé avec succès',"nom":nom})  
    except Exception as error:
        print("Erreur lors de la création du groupe", error)
        conn.rollback()  # Annuler en cas d'erreur
        return jsonify({"message': 'Erreur lors de la création de l'utilisateur"}), 500 
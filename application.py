from psycopg2 import DatabaseError,InterfaceError
from psycopg2.extensions import connection,cursor
import psycopg2
from flask import Flask,redirect,render_template,request,jsonify
import json
from app.users.route import *
from app.lib.bd import *



app = Flask(__name__)  

@app.route('/')
def list():
    users=list_user()
    return users

@app.route('/create_user', methods=['POST'])
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
        return jsonify({'message': 'Utilisateur créé avec succès'})  # Message de succès
    except Exception as error:
        print("Erreur lors de la création de l'utilisateur", error)
        conn.rollback()  # Annuler en cas d'erreur
        return jsonify({"message': 'Erreur lors de la création de l'utilisateur"}), 500  # Message d'erreur

if __name__ == '__main__':

    app.run(debug=True)
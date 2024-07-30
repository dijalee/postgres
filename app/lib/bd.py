
import psycopg
from flask import jsonify
from psycopg.rows import dict_row
try:
        conn=psycopg.connect(
            'postgres://{}:{}@localhost:5432/{}'.format("postgres", "postgres", "baseapi"),
            autocommit=True,
            row_factory=dict_row
        )
        cur=conn.cursor()
        
except(Exception,psycopg.Error) as error :
        print("Erreur lors connection à PostgreSQL",error)
        
        


def inserer_utilisateur(nom, prenom, email, mot_de_pass, role):
    try:
        cur.execute(
            """
            INSERT INTO utilisateur(nom_user, prenom, email, mot_de_passe,role)
            VALUES (%s, %s, %s, %s,%s)
            """,
            (nom, prenom, email, mot_de_pass,role)
        )
        conn.commit()
        print("Utilisateur inséré avec succès")
    except Exception as e:
        print(f"Erreur d'insertion de l'utilisateur: {e}")
        conn.rollback()
    
def inserer_groupe(nom):
    try:
        cur.execute("""INSERT INTO groupe(nom) values(%s)""",(nom,))
        conn.commit()
    except Exception as e:
        print(f"Erreur de creation du group",nom,": {e}")
        conn.rollback()

def lister_prompt():
    query="select *from prompt"
    cur.execute(query)
    
def ajout_prompt(titre,texte,statut,prix):
    cur.execute("""INSERT INTO prompt(titre,texte,statut,prix) values(%s,%s,%s,%s)""",(titre,texte,statut,prix))
    conn.commit()
    
        
def getUserByEmail(email):
    cur.execute("""select nom_user,prenom,email,role from utilisateur where email=%s""",(email,))
    result=cur.fetchone()
    print(result)
    return result

def get_role_by_email(email):
    cur.execute("""select role from utilisateur where email=%s""",(email,))
    result=cur.fetchone()
    print(result)
    return result

def supprimer_Prompt(id):
    cur.execute("""delete table promptcascade where id=%s""",(id,))   
    conn.commit()
    
def modification_prompt(titre,description,statut,id):
    query = "UPDATE prompt SET titre=%s, description=%s, statut=%s WHERE id_prompt=%s"
    params = (titre, description, statut, id,)

# Ensuite, vous exécuteriez cette requête avec vos paramètres
    cur.execute(query, params)
    
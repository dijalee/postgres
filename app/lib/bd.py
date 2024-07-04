
import psycopg2
try:
        conn=psycopg2.connect(
            user="postgres",
            password="postgres",
            host="localhost",
            port="5432",
            database="baseapi"
        )
        cur=conn.cursor()
except(Exception,psycopg2.Error) as error :
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


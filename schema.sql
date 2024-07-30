--Connexion à la base de données--
\c apidata;

CREATE TYPE user_role AS ENUM ('admin', 'user');

-- Création des tables
CREATE TABLE groupe (
    groupID SERIAL PRIMARY KEY,
    nom VARCHAR(25) NOT NULL 
);

CREATE TABLE utilisateur(
    id_user  SERIAL PRIMARY KEY,
    nom_user VARCHAR(100) NOT NULL,
    prenom varchar(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    mot_de_passe VARCHAR(100) NOT NULL,
    role user_role NOT NULL ,
    groupe_id INTEGER ,
    FOREIGN KEY(groupe_id)REFERENCES groupe(groupID),
    date_creation TIMESTAMP DEFAULT NOW()
);

CREATE TABLE Prompt (
    id_prompt SERIAL PRIMARY KEY,
    titre TEXT NOT NULL,
    texte VARCHAR(50) NOT NULL,
    statut varchar(10) NOT NULL,
    prix DECIMAL(10, 2) NOT NULL DEFAULT 1000.00,
    id_user int,
    FOREIGN KEY (id_user) REFERENCES utilisateur(id_user),
    date_creation TIMESTAMP DEFAULT NOW(),
    date_modification TIMESTAMP
);
drop table prompt CASCADE;
CREATE TABLE vote (
    id_vote  serial PRIMARY KEY,
    voteValue INT NOT NULL,
    id_user INT NOT NULL,
    id_prompt INT NOT NULL,
        FOREIGN KEY(id_user) 
        REFERENCES utilisateur(id_user) ON DELETE CASCADE,,
        FOREIGN KEY(id_prompt) ON DELETE CASCADE,
        REFERENCES Prompt(id_prompt)
);

CREATE TABLE note (
    id_note  serial PRIMARY KEY,
    noteValue INT NOT NULL,
    id_user INT NOT NULL,
    id_prompt INT NOT NULL,
        FOREIGN KEY(id_user) 
        REFERENCES utilisateur(id_user) ON DELETE CASCADE,,
        FOREIGN KEY(id_prompt) ON DELETE CASCADE,
        REFERENCES Prompt(id_prompt)
);

SELECT * from prompt;
select nom_user,prenom,email,role from utilisateur ;
INSERT INTO utilisateur(nom_user, prenom, email, mot_de_passe,role,groupe_id)
            VALUES ('fall','fatou','fall@gmail.com','1234567','user',5);
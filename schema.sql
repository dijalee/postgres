--Connexion à la base de données--
\c apidata;

CREATE TYPE user_role AS ENUM ('admin', 'user');

-- Création des tables
CREATE TABLE groupe (
    groupID SERIAL PRIMARY KEY,
    name VARCHAR(25) NOT NULL,
    user_id INT,
        FOREIGN KEY(uuser_id) 
        REFERENCES utilisateur(user_id)
);

CREATE TABLE utilisateur(
    id_user  SERIAL PRIMARY KEY,
    nom_user VARCHAR(100) NOT NULL,
    prenom varchar(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    mot_de_passe VARCHAR(100) NOT NULL,
    role user_role NOT NULL ,
    date_creation TIMESTAMP DEFAULT NOW()
);

CREATE TABLE Prompt (
    id_prompt SERIAL PRIMARY KEY,
    titre TEXT NOT NULL,
    texte VARCHAR(50) NOT NULL,
    statut varchar(10) NOT NULL,
    prix DECIMAL(10, 2) NOT NULL DEFAULT 1000.00,
    date_creation TIMESTAMP DEFAULT NOW(),
    date_modification TIMESTAMP
);

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
# Creation de la base de données
CREATE DATABASE mafiosa;

# Création des tables
USE mafiosa;

CREATE TABLE service (
    id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    nom VARCHAR(255) NOT NULL
);

CREATE TABLE employe (
    id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    nom VARCHAR(255) NOT NULL,
    prenom VARCHAR(255) NOT NULL,
    salaire DECIMAL NOT NULL,
    id_service INT NOT NULL,
    FOREIGN KEY (id_service) REFERENCES service(id)
);

# Remplissage des tables
INSERT INTO service (nom)
    VALUES
        ('Sicario'),  # Exécutions
        ('Logistique'),  # Transport et approvisionnement
        ('Ressources humaines'),  # Recrutement et gestion
        ('Finance');  # Gestion des fonds et blanchiment

INSERT INTO employe (nom, prenom, salaire, id_service)
    VALUES
        ('Corleone', 'Vito', 10000.00, 1),  -- Sicario
        ('Corleone', 'Michael', 15000.00, 4),  -- Finance
        ('DeVito', 'Tommy', 8000.00, 1),  -- Sicario
        ('Hill', 'Henry', 6000.00, 2),  -- Logistique
        ('Giuliano', 'Salvatore', 7000.00, 2),  -- Logistique
        ('Gotti', 'John', 12000.00, 4),  -- Finance
        ('Luciano', 'Lucky', 11000.00, 3),  -- Ressources humaines
        ('Costello', 'Frank', 13000.00, 4),  -- Finance
        ('Montana', 'Tony', 9000.00, 1),  -- Sicario
        ('Lansky', 'Meyer', 14000.00, 4);  -- Finance

# Requête SQL pour obtenir les mafieux payés au moins 10000 dollars
SELECT *
FROM employe
WHERE salaire >= 10000.00;

# Enregistrer la table
mysqldump -u root -p mafiosa > mafiosa.sql
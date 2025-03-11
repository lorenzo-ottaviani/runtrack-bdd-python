"""
Auteur : Lorenzo OTTAVIANI
Date : 11/03/2025 11h57
But du programme :
    Imprime le contenu de la table etudiant de la base de données LaPlateforme.
Entrée : Base de données SQL LaPlateforme.
Sortie : Contenu de la table etudiant.
"""

import mysql.connector
from dotenv import find_dotenv, load_dotenv
from os import getenv

# Charger les variables d'environnement depuis le fichier .env
dotenv_path = find_dotenv(".env")
load_dotenv(dotenv_path)

# Accéder aux variables d'environnement
my_host = getenv("HOST")
my_user = getenv("USER")
my_password = getenv("PASSWORD")
my_database = getenv("DATABASE_NAME")

# Connection au serveur
ma_base = mysql.connector.connect(
    host=my_host,
    user=my_user,
    password=my_password,
    database=my_database
)

# Récupérer un curseur
curseur = ma_base.cursor()

# Exécuter une requête
curseur.execute("SELECT * FROM etudiant")

# Récupérer toute la table
etudiants = curseur.fetchall()
print(etudiants)

# Fermer le curseur et la base
curseur.close()
ma_base.close()

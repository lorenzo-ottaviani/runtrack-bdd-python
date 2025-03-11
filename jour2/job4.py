"""
Auteur : Lorenzo OTTAVIANI
Date : 11/03/2025 14h09
But du programme :
    Imprime les colonnes nom et capacité de la table salle de la base de données LaPlateforme.
Entrée : Base de données SQL LaPlateforme.
Sortie : Colonnes nom et capacité de la table salle.
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

# Exécuter ma requête
curseur = ma_base.cursor()
curseur.execute("SELECT nom, capacite FROM salle")

salles = curseur.fetchall()
for salle in salles:
    print(f"La salle {salle[0]} a une capacité de {salle[1]} places.")

# Fermer le curseur et la base
curseur.close()
ma_base.close()

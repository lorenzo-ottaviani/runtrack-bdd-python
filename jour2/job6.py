"""
Auteur : Lorenzo OTTAVIANI
Date : 11/03/2025 14h52
But du programme :
    Capacité totale de la table salle de la base de données LaPlateforme.
Entrée : Base de données SQL LaPlateforme.
Sortie : Capacité totale.
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
curseur.execute("SELECT SUM(capacite) FROM salle")

capacite_totale = curseur.fetchone()
print(f"La capacité de toutes les salles est de {capacite_totale[0]} places.")

# Fermer le curseur et la base
curseur.close()
ma_base.close()

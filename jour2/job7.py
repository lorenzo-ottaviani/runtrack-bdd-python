"""
Auteur : Lorenzo OTTAVIANI
Date : 11/03/2025 23h50
But du programme :
    Gérer la table "employe" de la base de données "mafiosa" avec une classe.
Entrée : Base de données SQL mafiosa.
Sortie : Tests des requêtes permettant de gérer la table.
"""

import mysql.connector
from dotenv import find_dotenv, load_dotenv
from os import getenv

# Charger les variables d'environnement depuis le fichier .env
dotenv_path = find_dotenv(".env")
load_dotenv(dotenv_path)

# Accéder aux variables d'environnement
my_host = getenv("HOST")
my_port = getenv("PORT")
my_user = getenv("USER")
my_password = getenv("PASSWORD")


class Employe:
    """ Classe pour gérer la table des employés. """

    def __init__(self):
        """ Initialisation de la classe. """
        self.ma_base = mysql.connector.connect(
            host=my_host,
            port=my_port,
            user=my_user,
            password=my_password,
            database="mafiosa"
        )

    def create(self, ligne):
        """
        Ajoute une nouvelle ligne à la fin de la table.
        :param ligne: Le contenu de la ligne à ajouter, sous forme de tuple.
        :return: ∅
        """
        curseur = self.ma_base.cursor()
        curseur.execute(f"INSERT INTO employe(nom, prenom, salaire, id_service) VALUES {ligne}")
        self.ma_base.commit()  # Sauvegarde dans la base
        curseur.close()

    def read(self, id_ligne):
        """
        Lit une ligne de la table.
        :param id_ligne: Id unique de la ligne.
        :return: ∅
        """
        curseur = self.ma_base.cursor()
        curseur.execute(f"SELECT * FROM employe WHERE id = {id_ligne}")
        ligne = curseur.fetchone()
        print(f"Id : {ligne[0]}\nNom : {ligne[1]}\nPrénom : {ligne[2]}\nSalaire : {ligne[3]}\nId_Service : {ligne[4]}")
        self.ma_base.commit()  # Sauvegarde dans la base
        curseur.close()

    def update(self, changement, id_ligne):
        """
        Modifie une ligne de la table.
        :param changement: Changement à effectuer, sous la forme colonne = nouvelle valeur.
        :param id_ligne: Id unique de la ligne.
        :return: ∅
        """
        curseur = self.ma_base.cursor()
        curseur.execute(f"UPDATE employe SET {changement} WHERE id = {id_ligne}")
        self.ma_base.commit()  # Sauvegarde dans la base
        curseur.close()

    def delete(self, id_ligne):
        """
        Supprime une ligne de la table.
        :param id_ligne: Id unique de la ligne.
        :return: ∅
        """
        curseur = self.ma_base.cursor()
        curseur.execute(f"DELETE FROM employe WHERE id = {id_ligne}")
        self.ma_base.commit()  # Sauvegarde dans la base
        curseur.close()

    def employees_et_services(self):
        """
        Récupère tous les employés et leur service respectif.
        :return: ∅
        """
        curseur = self.ma_base.cursor()
        curseur.execute("SELECT e.nom, e.prenom, e.salaire, s.nom AS service FROM employe e "
                        "JOIN service s ON e.id_service = s.id")
        lignes = curseur.fetchall()
        for ligne in lignes:
            print(f"Nom: {ligne[0]}, Prénom: {ligne[1]}, Salaire: {ligne[2]}, Service: {ligne[3]}")


# Tests
mafia_manageur = Employe()
mafia_manageur.create(('Dupont', 'Jean', 3000.00, 2))
mafia_manageur.read(27)
mafia_manageur.update("salaire=5000.00", 27)
mafia_manageur.read(27)
mafia_manageur.delete(27)
mafia_manageur.employees_et_services()

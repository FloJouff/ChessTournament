from models.player import Player
from datetime import datetime
import re
import json


class PlayerView:
    def afficher_player(self):
        print(Player.name, Player.first_name, Player.score)

    def afficher_list_players(self, players: [Player]):
        print("Afficher tous les joueurs: ")
        i = 0
        for player in players:
            print(i, player.name, player.first_name)
            i = i + 1

    def validation_ine(new_ine):
        # Verification que l'INE indiqué n'existe pas déjà:
        with open("data/player_data.json", "r") as f:
            data = json.load(f)

            if any(element.get('ine') == new_ine for element in data):
                print(f"Cet INE {new_ine} existe déjà dans le fichier json")
                return False

        # Vérification que le format de l'INE est correct:
        pattern = re.compile(r"^[A-Za-z]{2}\d{5}$")

        if pattern.match(new_ine):
            return True
        else:
            print("Format invalide. Utilisez 2 lettres suivies de 5 chiffres.")
            return False

    def validation_date(date_str):
        try:
            # Convertir la chaîne en objet datetime
            date_obj = datetime.strptime(date_str, "%d/%m/%Y")

            # Vérifier si la date est dans une plage raisonnable.
            date_min = datetime(1900, 1, 1)
            date_max = datetime.now()

            if date_min <= date_obj <= date_max:
                return True
            else:
                print("La date doit être comprise entre 01/01/1900 et aujourd'hui.")
                return False

        except ValueError:
            print("Format de date invalide. Utilisez le format JJ/MM/AAAA.")
            return False

    def get_player_infos(self):
        print("Veuillez rentrer les informations du joueur: ")
        name = input("Nom: ")
        first_name = input("Prénom: ")
        gender = input("Sexe: ")
        while True:
            date_of_birth = input("Date de naissance: (format JJ/MM/AAAA)")     
            if PlayerView.validation_date(date_of_birth):
                break
        while True:
            ine = input("indiquez votre ine: (format: 2lettres5chiffres)")
            if PlayerView.validation_ine(ine):
                break
        return {
            "name": name,
            "first_name": first_name,
            "gender": gender,
            "date_of_birth": date_of_birth,
            "ine": ine,
        }

    def menu_player(self):
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("----------------  MENU DES JOUEURS  ---------------")
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("1 --> Pour Ajouter un joueur")
        print("2 --> Pour afficher tous les joueurs")
        print("0 --> Quitter")
        return input("Votre choix: ")

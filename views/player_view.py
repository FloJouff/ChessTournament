from models.player import Player
import Constantes.constantes as constante
from datetime import datetime
from typing import List


class PlayerView:
    def afficher_player(self):
        """display a player"""
        print(Player.name, Player.first_name, Player.score)

    def display_list_players(self, players: List[Player]):
        """Display list of all players

        Args:
            players (List[Player])
        """
        print("Afficher tous les joueurs: ")
        i = 0
        for player in players:
            print(i, "Nom: ", player.name, "  Prénom: ", player.first_name, "INE: ", player.ine)
            i = i + 1

    def date_validation(date_str):
        """Validate date format

        Args:
            date_str (str): date
        """
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
        """Get new player's datas

        Returns:
            player's datas
        """
        print("Veuillez rentrer les informations du joueur: ")
        name = input("Nom: ")
        first_name = input("Prénom: ")
        gender = input("Sexe: ")
        while True:
            date_of_birth = input("Date de naissance: (format JJ/MM/AAAA)")
            if PlayerView.date_validation(date_of_birth):
                break
        while True:
            ine = input("indiquez votre ine: (format: 2lettres5chiffres)")
            if Player.ine_validation(ine):
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
        print(f"{constante.ADD_PLAYER} --> Pour Ajouter un joueur")
        print(f"{constante.DISPLAY_PLAYERS} --> Pour afficher tous les joueurs")
        print(f"{constante.DISPLAY_PLAYER_BY_INE} --> Rechercher un joueur par son INE :")
        print("0 --> Retour au menu précédent")
        print("")
        return input("Votre choix: ")

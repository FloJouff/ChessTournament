from models.player import Player


class PlayerView:
    def afficher_player(self):
        pass

    def afficher_list_players(self, players: [Player]):
        print("Afficher tous les joueurs: ")
        for player in players:
            print(player['name'], player['surname'])

    def get_player_infos(self):
        print("Rentrer les infos des joueurs: ")
        name = input("Nom du joueur:")
        surname = input("Prénom: ")
        gender = input("Sexe: ")
        date_of_birth = input("Date de naissance: ")
        return {name, surname, gender, date_of_birth}

    def menu_player(self):
        print("Menu Player")
        print("1. Pour Ajouter un joueur")
        print("2. Pour lister tous les joueurs")
        print("0. Quitter")
        return input("Votre choix: ")


"""Affiche les informations liées aux joueurs ainsi
que les demandes d'informartions relatives aux joueurs
input[nom du joueur]...

print( le joueur{nom} a {score} points à l'issu du tour {numero du tour})
"""

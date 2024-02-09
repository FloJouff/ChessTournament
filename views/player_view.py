from models.player import Player


class PlayerView:
    def afficher_player(self):
        print(Player.name, Player.first_name, Player.score)

    def afficher_list_players(self, players: [Player]):
        print("Afficher tous les joueurs: ")
        for player in players:
            print(player.name, player.first_name)

    def get_player_infos(self):
        print("Veuillez rentrer les informations du joueur: ")
        name = input("Nom: ")
        surname = input("Prénom: ")
        gender = input("Sexe: ")
        date_of_birth = input("Date de naissance: ")
        return (name, surname, gender, date_of_birth)

    def menu_player(self):
        print("--------------------Menu Player--------------------")
        print("1. Pour Ajouter un joueur")
        print("2. Pour lister tous les joueurs")
        print("0. Quitter")
        return input("Votre choix: ")

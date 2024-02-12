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
        first_name = input("Prénom: ")
        gender = input("Sexe: ")
        date_of_birth = input("Date de naissance: ")
        return {"name": name, "first_name": first_name, "gender": gender,
                "date_of_birth": date_of_birth}

    def menu_player(self):
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("----------------  MENU DES JOUEURS  ---------------")
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("1 --> Pour Ajouter un joueur")
        print("2 --> Pour afficher tous les joueurs")
        print("0 --> Quitter")
        return input("Votre choix: ")

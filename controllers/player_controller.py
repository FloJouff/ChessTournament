from views.player_view import PlayerView
from models.player import Player


class PlayerController:
    def __init__(self) -> None:
        self.playerview = PlayerView()

    def run_player(self):
        choix = ""
        while (choix != "0"):
            choix = self.playerview.menu_player()
            if choix == "1":
                data = self.playerview.get_player_infos()
                print(data)
                player = Player(data["name"], data["first_name"],
                                data["gender"],
                                data["date_of_birth"])
                player.save()
            elif choix == "2":
                players = Player.load_all_players()
                self.playerview.afficher_list_players(players)
            elif choix == "0":
                print("Quitter")
                break

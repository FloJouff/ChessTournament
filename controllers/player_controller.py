from views.player_view import PlayerView
from models.player import Player
import Constantes.constantes as constante


class PlayerController:
    def __init__(self) -> None:
        self.playerview = PlayerView()

    def run_player(self):
        choix = ""
        while choix != "0":
            choix = self.playerview.menu_player()
            if choix == constante.ADD_PLAYER:
                data = self.playerview.get_player_infos()
                print(data)
                player = Player(data["name"], data["first_name"], data["gender"], data["date_of_birth"], data["ine"])
                player.save()
            elif choix == constante.DISPLAY_PLAYERS:
                players = Player.load_all_players(self)
                self.playerview.display_list_players(players)
            elif choix == constante.DISPLAY_PLAYER_BY_INE:
                ine = input("Veuillez saisir l'INE du joueur recherché: ")
                player = Player.load_player_by_ine(ine)
                print(player)
            elif choix == "0":
                print("Quitter")
                break

from views.tournament_view import TournamentView
from models.player import Player
from models.tournament import Tournament


class TournamentController:
    def __init__(self) -> None:
        self.tournamentview = TournamentView()

    def run_tournament(self,):
        choix = ""
        while (choix != "0"):
            choix = self.tournamentview.menu_tournoi()
            if choix == "1":
                data = self.tournamentview.get_tournament_infos()
                print(data)
                tournoi = Tournament(data["name"], data["place"], data["dates"])
                tournoi.save()
            elif choix == "2":
                TournamentView.register_player()
            elif choix == "3":
                pass
            elif choix == "4":
                data["description"] = input("Veuillez rentrer une description du tournoi: ")
            elif choix == "0":
                print("Quitter")
                break

    def round_management():
        pass

from views.report_view import ReportView
from models.report import Report
from models.player import Player
import json
""" Gère la génération des rapports demandés"""


class ReportController:
    def __init__(self) -> None:
        self.reportview = ReportView()

    def run_report(self):
        choix = ""
        while (choix != "0"):
            choix = self.reportview.menu_report()
            if choix == "1":
                data = Report.display_tournaments()
                print(data)
            elif choix == "2":
                data = Player.load_all_players()
                print("Liste de tous les joueurs enregistrés dans le fichier: ")
                print(data)
                print("")
            elif choix == "3":
                place = input("Pour quel tournoi souhaitez vous avoir ces informations? ")
                data = Report.load_tournament_by_place(place)
                print(data)
                print("")
            elif choix == "4":
                place = input("De quel tournoi souhaitez vous avoir la liste des participants? ")
                data = Report.get_tournament_participants_by_place(place)
                print(data)
                print("")
            elif choix == "5":
                place = input("De quel tournoi souhaitez vous connaitre le nombre de tours? ")
                data = Report.get_tournament_numb_of_round_by_place(place)
                print(data)
                print("")
            elif choix == "6":
                place = input("De quel tournoi souhaitez vous connaitre les résultats? ")
                pass
            elif choix == "0":
                print("Quitter")
                break

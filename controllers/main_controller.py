from controllers.tournament_controller import TournamentController
from controllers.player_controller import PlayerController
from controllers.report_controller import ReportController
from views.main_view import MainView
""" Controlleur principal qui gère les interactions
entre les vues et les autres controlleurs

sauvegarde auto
génération des rapports
"""


class MainController():
    def __init__(self) -> None:
        self.playercontroller = PlayerController()
        self.tournamentcontroller = TournamentController()
        self.reportcontroller = ReportController()
        self.mainview = MainView()

    def run_main_controller(self):
        choix = ""
        while (choix != "0"):
            choix = self.mainview.menu_principal()
            if choix == "1":
                self.playercontroller.run_player()
            elif choix == "2":
                self.tournamentcontroller.run_tournament()
            elif choix == "3":
                self.reportcontroller.run_report()
            elif choix == "0":
                print("Quitter")
                break

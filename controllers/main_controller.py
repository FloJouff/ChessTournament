from controllers.tournament_controller import TournamentController
from controllers.player_controller import PlayerController
from controllers.report_controller import ReportController
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
        self.mainview

    def run_main_controller(self):
        choix = ""
        while (choix != "0"):
            choix = self.mainview.menu_principal()
            if choix == "1":
                self.playercontroller.run()
            elif choix == "2":
                self.tournamentcontroller.run()
            elif choix == "3":
                self.reportcontroller.run()
            elif choix == "0":
                print("Quitter")
                break

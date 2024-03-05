from controllers.tournament_controller import TournamentController
from controllers.player_controller import PlayerController
from controllers.report_controller import ReportController
from views.main_view import MainView
import Constantes.constantes as constante

""" Controlleur principal qui gère les interactions
entre les vues et les autres controlleurs
"""


class MainController:
    def __init__(self) -> None:
        self.playercontroller = PlayerController()
        self.tournamentcontroller = TournamentController()
        self.reportcontroller = ReportController()
        self.mainview = MainView()

    def run_main_controller(self):
        choix = ""
        while choix != "0":
            choix = self.mainview.menu_principal()
            if choix == constante.PLAYER_MENU:
                self.playercontroller.run_player()
            elif choix == constante.TOURNAMENT_MENU:
                self.tournamentcontroller.run_tournament()
            elif choix == constante.REPORT_MENU:
                self.reportcontroller.run_report()
            elif choix == "0":
                print("Quitter")
                break

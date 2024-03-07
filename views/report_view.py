import Constantes.constantes as constante
from models.report import Report


class ReportView:
    def menu_report(self):
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("-----------------MENU DES RAPPORTS-----------------")
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
        print(f"{constante.DISPLAY_TOURNAMENT_LIST} --> Pour afficher la liste des tournois enregistrés")
        print(f"{constante.DISPLAY_PLAYERS_LIST} --> Pour afficher la liste de tous les joueurs")
        print(f"{constante.DISPLAY_TOURNAMENT_NAME_DATES} --> Pour afficher le nom et les dates d'un tournoi")
        print(f"{constante.DISPLAY_TOURNAMENT_LIST_PLAYER} --> Pour afficher la liste des joueurs d'un tournoi")
        print(f"{constante.DISPLAY_TOURNAMENT_NUMBER_OF_ROUND} --> Pour afficher le nombre de tours d'un tournoi")
        print(f"{constante.DISPLAY_TOURNAMENT_LIST_OF_MATCHS} --> Pour afficher la liste des matchs d'un tour")
        print("0 --> Retour au menu précédent")
        print("")
        return input("Votre choix: ")

    def get_input(self):
        print("Liste des tournois: ")
        tournoi = Report.display_tournaments(self)
        print("")
        choice = input("Pour quel tournoi souhaitez vous ces informations? ")
        id_tournoi = tournoi[int(choice)]["id"]
        return id_tournoi

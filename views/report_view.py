import Constantes.constantes as constante


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

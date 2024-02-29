

class ReportView:
    def menu_report(self):
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("-----------------MENU DES RAPPORTS-----------------")
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("1 --> Pour afficher la liste des tournois enregistrés")
        print("2 --> Pour afficher la liste de tous les joueurs")
        print("3 --> Pour afficher le nom et les dates d'un tournoi")
        print("4 --> Pour afficher la liste des joueurs d'un tournoi")
        print("5 --> Pour afficher le nombre de tours d'un tournoi")
        print("6 --> Pour afficher la liste des matchs d'un tour")
        print("0 --> Retour au menu précédent")
        print("")
        return input("Votre choix: ")

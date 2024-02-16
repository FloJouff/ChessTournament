

class ReportView:
    def menu_report(self):
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("-----------------MENU DES RAPPORTS-----------------")
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("1 --> Pour afficher la liste des tournois enregistrés")
        print("2 --> Pour afficher la liste de tous les joueurs")
        print("3 --> Pour afficher le nom et les dates d'un tournoi")
        print("4 --> Pour afficher la liste des joueurs de ce tournoi")
        print("5 --> Pour afficher la liste des tours et des matchs de ce tournoi")
        print("0 --> Quitter")
        print("")
        return input("Votre choix: ")

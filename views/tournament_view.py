from models.tournament import Tournament


class TournamentView:
    def afficher_tournoi(self):
        print(Tournament.name, Tournament.place)

    def get_tournament_infos(self):
        print("Rentrer les infos du tournois ")
        name = input("Nom du tournoi:")
        place = input("Lieu: ")
        start_date = input("Date de début: ")
        end_date = input("Date de fin: ")
        return {name, place, start_date, end_date}

    def menu_tournoi(self):
        print("Menu tournoi")
        print("1. Pour enregistrer les informations d'un tournoi")
        print("2. Pour inscrire un participant à ce tournoi")
        print("3. Pour afficher les scores d'un tournoi")
        print("4. Pour saisir une description ")
        print("0. Quitter")
        return input("Votre choix: ")

""" Affiche les informations liées aux tournois et les demandes
    d'informations relatives à ceux ci

    input(nom du tournoi, date, lieu...)    
"""

from models.tournament import Tournament
from views.player_view import PlayerView


class TournamentView:
    def __init__(self) -> None:
        self.tournament = Tournament("Chess Tour-nament", "Tour", "12/10/2022",
                                     "14/10/2022")

    def afficher_tournoi(self):
        print(Tournament.name, Tournament.place)

    def get_tournament_infos(self):
        print("Rentrer les informations du tournoi ")
        name = input("Nom du tournoi:")
        place = input("Lieu: ")
        while True:
            start_date = input("Date de début: ")
            if PlayerView.validation_date(start_date):
                break
        while True:
            end_date = input("Date de fin: ")
            if PlayerView.validation_date(end_date):
                break
        number_of_round = input("Nombre de tour pour ce tournoi: ")
        return {"name": name, "place": place,
                "start_date": start_date, "end_date": end_date,
                "nombre_de_tour": number_of_round}

    def menu_tournoi(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("---------------  MENU DES TOURNOIS  ----------------")
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("1 --> Pour enregistrer les informations d'un tournoi ")
        print("2 --> Pour afficher la liste des participants ")
        print("3 --> Pour démarrer un nouveau tour et générer les matchs ")
        print("4 --> Pour résoudre aléatoirement les matchs du tour ")
        print("5 --> Pour cloturer un tour ")
        print("6 --> Pour saisir une description ")
        print("0 --> Quitter")
        return input("Votre choix: ")


class MatchView:
    def afficher_match(player1, player2):
        print(player1, " vs ", player2)

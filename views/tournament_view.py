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
                "nombre_de_tour": number_of_round, "description": ""}

    def menu_tournoi(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("---------------  MENU DES TOURNOIS  ----------------")
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("1 --> Pour enregistrer les informations d'un tournoi ")
        print("2 --> Pour afficher la liste des participants ")
        print("3 --> Pour démarrer un nouveau tour et générer les matchs ")
        print("4 --> Pour saisir les résultats des matchs du tour 1")
        print("5 --> Pour saisir les résultats des matchs des autres tours")
        print("6 --> Pour cloturer un tour ")
        print("7 --> Pour saisir une description ")
        print("0 --> Quitter")
        print("")
        return input("Votre choix: ")


class MatchView:
    def afficher_match(player1, player2):
        print(player1, " vs ", player2)

    def match_results_entry(player1, player2):
        result = input(f"Veuillez indiquer le resultat du match entre {player1[0]} et {player2[0]} (J1, J2 ou nul): ")
        if result == "J1":
            player1[1] = player1[1] + 1
        elif result == "J2":
            player2[1] = player2[1] + 1
        elif result == "nul":
            player1[1] = player1[1] + 0.5
            player2[1] = player2[1] + 0.5
        else:
            print("Saisie incorrecte")

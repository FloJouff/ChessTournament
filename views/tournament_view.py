from models.tournament import Tournament
from views.player_view import PlayerView


class TournamentView:
    def __init__(self) -> None:
        self.tournament = Tournament("Chess Tour-nament", "Tour", "12/10/2022",
                                     "14/10/2022", "")

    def display_tournament(self):
        print(self.name, self.place)

    def get_tournament_infos(self):
        print("Rentrer les informations du tournoi ")
        name = input("Nom du tournoi:")
        place = input("Lieu: ")
        while True:
            start_date = input("Date de début: ")
            if PlayerView.date_validation(start_date):
                break
        while True:
            end_date = input("Date de fin: ")
            if PlayerView.date_validation(end_date):
                break
        description = input("Tapez votre commentaire concernant ce tournoi: ")
        number_of_round = input("Nombre de tour pour ce tournoi: ")
        return {"name": name, "place": place,
                "start_date": start_date, "end_date": end_date,
                "number_of_round": number_of_round, "description": description}

    def menu_tournoi(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("---------------  MENU DES TOURNOIS  ----------------")
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("1 --> Pour enregistrer les informations d'un nouveau tournoi ")
        print("2 --> Pour afficher la liste des tournois ")
        print("3 --> Pour charger les données d'un tournoi enregistré: ")
        print("4 --> Pour lancer un nouveau tournoi ")
        print("5 --> Pour reprendre un tournoi en cours. ")
        print("0 --> Retour au menu précédent")
        print("")
        return input("Votre choix: ")


class MatchView:
    def display_match(player1, player2):
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

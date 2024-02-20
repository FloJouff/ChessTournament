from models.tournament import Tournament
from views.player_view import PlayerView
import json


class TournamentView:
    def __init__(self) -> None:
        self.tournament = Tournament("Chess Tour-nament", "Tour", "12/10/2022",
                                     "14/10/2022")

    def display_tournament(self):
        print(Tournament.name, Tournament.place)

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
        number_of_round = input("Nombre de tour pour ce tournoi: ")
        return {"name": name, "place": place,
                "start_date": start_date, "end_date": end_date,
                "nombre_de_tour": number_of_round, "description": ""}

    def get_description(self):
        with open("data/tournaments.json", "r") as f:
            data = json.load(f)
        tournament_data = Tournament.to_dict()
        data["description"] = input("Tapez votre commentaire concernant ce tournoi: ")
        data.append(tournament_data)
        with open("data/tournaments.json", "w") as f:
            json.dump(data, f, indent=4)
        print(data["description"])

    def menu_tournoi(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("---------------  MENU DES TOURNOIS  ----------------")
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("1 --> Pour enregistrer les informations d'un tournoi ")
        print("2 --> Pour afficher la liste des participants ")
        print("3 --> Pour démarrer un nouveau tour et générer les matchs ")
        print("4 --> Pour saisir les résultats des matchs du tour ")
        print("5 --> Pour cloturer un tour ")
        print("6 --> Pour saisir une description ")
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

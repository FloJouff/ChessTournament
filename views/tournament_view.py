from models.tournament import Tournament
from views.player_view import PlayerView
import Constantes.constantes as constante


class TournamentView:
    def __init__(self) -> None:
        self.tournament = Tournament("", "", "", "", "")

    def display_tournament(self):
        """Display tournament name and place"""
        print(self.name, self.place)

    def get_tournament_infos(self):
        """Get tournament datas

        Returns:
            dict: tournament key/value
        """
        print("Rentrer les informations du tournoi ")
        name = input("Nom du tournoi:")
        place = input("Lieu: ")
        while True:
            start_date = input("Date de début: (format JJ/MM/AAAA)")
            if PlayerView.date_validation(start_date):
                break
        while True:
            end_date = input("Date de fin: (format JJ/MM/AAAA)")
            if PlayerView.date_validation(end_date):
                break
        description = input("Tapez votre commentaire concernant ce tournoi: ")
        number_of_round = input("Nombre de tour pour ce tournoi (4 par défaut): ")
        if number_of_round == "":
            number_of_round = 4
        return {
            "name": name,
            "place": place,
            "start_date": start_date,
            "end_date": end_date,
            "number_of_round": number_of_round,
            "description": description,
        }

    def menu_tournoi(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("---------------  MENU DES TOURNOIS  ----------------")
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print(f"{constante.CREATE_TOURNAMENT} --> Pour enregistrer les informations d'un nouveau tournoi ")
        print(f"{constante.DISPLAY_TOURNAMENTS} --> Pour afficher la liste des tournois ")
        print(f"{constante.START_NEW_TOURNAMENT} --> Pour lancer un nouveau tournoi ")
        print(f"{constante.RESUME_TOURNAMENT} --> Pour reprendre un tournoi en cours. ")
        print("0 --> Retour au menu précédent")
        print("")
        return input("Votre choix: ")


class MatchView:
    def display_match(player1, player2):
        """Display match players

        Args:
            player1 (object Player)
            player2 (object Player)
        """
        print(player1, " vs ", player2)

    def match_results_entry(player1, player2):
        """Entering match results

        Args:
            player1 (object Player)
            player2 (object Player)
        """
        while True:
            result = input(f"Veuillez indiquer le resultat du match {player1[0]} vs {player2[0]} (J1, J2 ou nul): ")
            result_lower = result.lower()
            if result_lower == "j1":
                player1[1] = player1[1] + 1
                print(f"Vainqueur: {player1[0]}")
                break
            elif result_lower == "j2":
                player2[1] = player2[1] + 1
                print(f"Vainqueur: {player2[0]}")
                break
            elif result_lower == "nul":
                player1[1] = player1[1] + 0.5
                player2[1] = player2[1] + 0.5
                print(f"Match nul. Les joueurs {player1[0]} et {player2[0]} gagnent 0.5 points")
                break
            else:
                print("Saisie incorrecte")

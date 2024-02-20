from models.tournament import Tournament
import json

"""
dans les rapports:
listes joueurs par ordre alphabétiques
listes des tournois
listes des joueurs d'un tournoi
liste de tous les tours d'un tournoi et de tous les matchs d'un tour
nom et date de tous les tournois

--> exporté en .txt ou .html
"""


class Report:
    def all_players_list_report():
        with open("data/player_data.json", "r") as f:
            data = json.loads(f.read())
            print(data)

    def display_tournaments():
        with open("data/tournaments.json", "r") as f:
            data = json.loads(f.read())
            print(data)

    def load_tournament_by_place(place):
        tournament = None
        with open("data/tournaments.json", "r") as f:
            data = json.load(f)
            for tournament_dict in data:
                if tournament_dict['place'] == place:
                    tournament = print(f"Le tournoi {tournament_dict["name"]}, situé à {tournament_dict["place"]}, a eu lieu du {tournament_dict["start_date"]} au {tournament_dict["end_date"]}")
                    break
        return tournament

    def get_tournament_participants_by_place(place):
        tournament = None
        with open("data/tournaments.json", "r") as f:
            data = json.load(f)
            for tournament_dict in data:
                if tournament_dict['place'] == place:
                    tournament = tournament_dict['players']
                    break
        tournament.sort()
        return tournament

    def get_tournament_numb_of_round_by_place(place):
        tournament = None
        with open("data/tournaments.json", "r") as f:
            data = json.load(f)
            for tournament_dict in data:
                if tournament_dict['place'] == place:
                    tournament = tournament_dict['nombre_de_tour']
                    break
        return tournament

    def display_matches_per_round(name, round_nb):
        tournament = None
        with open("data/tournaments.json", "r") as f:
            data = json.load(f)
            for tournament_dict in data:
                if tournament_dict['name'] == name & tournament_dict['round_nb'] == round_nb:
                    tournament = tournament_dict['matches']
                    break
        return tournament

    def save_matches():
        with open("data/tournaments.json", "r") as f:
            data = json.load(f)
        tournament_data = Tournament.to_dict()
        data.append(tournament_data)
        with open("data/tournaments.json", "w") as f:
            json.dump(data, f, indent=4)

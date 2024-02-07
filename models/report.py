from player import player_list
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
    def tournament_player_list_report():
        print(player_list['name'].sort())

    def all_players_list_report():
        with open("data/player_data.json", "r") as f:
            data = json.loads(f.read())
            print(data)

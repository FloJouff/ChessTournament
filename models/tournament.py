import json
from models.player import Player

from datetime import datetime


class Tournament:
    def __init__(self, name, place, start_date, end_date, players=[],
                 number_of_round=4):
        self.name = name
        self.place = place
        self.start_date = start_date
        self.end_date = end_date
        self.current_round_number = int
        self.players = players
        self.number_of_round = number_of_round
        self.description = str

    def __str__(self):
        return f"Bienvenue au tournoi {self.name}, a {self.place}"

    def __repr__(self):
        return f"({self.name}, {self.place})"

    def create_tournament(self):
        tournament = {"name": self.name, "place": self.place,
                      "start_date": self.start_date, "end_date": self.end_date,
                      "nombre de tour": self.number_of_round}
        tournament_data = json.dumps(tournament, indent=4)
        with open("data/tournaments.json", "a") as f:
            f.write(tournament_data)

    def add_tournament_players(self):
        self.players.append(Player.name)
        Player.score = 0.0
        new_list = [(nom, Player.score) for nom in self.players]
        for tuple in new_list:
            print(tuple)
        return new_list

# un tour = une liste de match


class Round:
    def __init__(self, round_number):
        self.round_number = round_number
        self.match_list = []

# incription de l'heure du début du tour.

    def creation_round(self):
        print("Début d'un nouveau tour")
        start_time_date = datetime.now()
        print(f"Heure de début du tour {self.round_number}: ", start_time_date)

# incription de l'heure du fin du tour.

    def round_closure(self):
        print("Fin du tour")
        round_end_time = datetime.now()
        print(f"le tour {self.round_number} s'est terminé à :", round_end_time)


""" tenir compte du fait qu'il y a en moyenne 4 tours par tournoi!!!!"""


class Match:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def __repr__(self):
        return f"({self.player1[0]} vs {self.player2[0]})"


# player1_name = input("Nom du joueur: ")
# player1_score = float(input("Score actuel du joueur 1: "))
# player2_name = input("Nom du joueur: ")
# player2_score = float(input("Score actuel du joueur 2: "))
# player1 = [player1_name, player1_score]
# player2 = [player2_name, player2_score]
# match = Match(player1, player2)

# print(match)

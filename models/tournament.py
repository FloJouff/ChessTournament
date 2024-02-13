import json
from datetime import datetime
from models.player import Player


class Tournament:
    def __init__(self, name, place, start_date, end_date, number_of_round=4):
        self.name = name
        self.place = place
        self.start_date = start_date
        self.end_date = end_date
        self.current_round_number = int
        self.players = [Player]
        self.number_of_round = number_of_round
        self.description = str

    def __str__(self):
        return f"Bienvenue au tournoi {self.name}, a {self.place}"

    def to_dict(self):
        return {"name": self.name, "place": self.place,
                "start_date": self.start_date, "end_date": self.end_date,
                "nombre_de_tour": self.number_of_round,
                "description": self.description}

    def create_tournament(self):
        with open("data/tournaments.json", "r") as f:
            data = json.load(f)
        tournament_data = self.to_dict()
        data.append(tournament_data)
        with open("data/tournaments.json", "w") as f:
            json.dump(data, f, indent=4)

    def generate_list_of_player():
        with open("data/player_data.json", "r") as f:
            data = json.load(f)
        player_list = [[item['name'], 0.0]
                       for item in data]
        print(player_list)
        return player_list


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

    def round_closure():
        print("Fin du tour")
        round_end_time = datetime.now()
        print("le tour en cours s'est terminé à :", round_end_time)


class Match:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def __str__(self):
        return f"({self.player1[0]} vs {self.player2[0]})"

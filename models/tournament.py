import json


class Tournament:
    def __init__(self, name, place, start_date, end_date,
                 current_round_number, list_of_players, description,
                 number_of_round=4):
        self.name = name
        self.place = place
        self.start_date = start_date
        self.end_date = end_date
        self.current_round_number = current_round_number
        self.list_of_players = list_of_players
        self.number_of_round = number_of_round
        self.description = description

    def __str__(self):
        return f"Bienvenue au tournoi {self.name}, qui a lieu a {self.place}"

    def create_tournament(self):
        tournament = {"name": self.name, "place": self.place,
                      "start_date": self.start_date, "end_date": self.end_date,
                      "nombre de tour": self.number_of_round}
        tournament_data = json.dumps(tournament, indent=4)
        with open("data/tournaments.json", "a") as f:
            f.write(tournament_data)

    def add_players(self):
        self.list_of_players = []

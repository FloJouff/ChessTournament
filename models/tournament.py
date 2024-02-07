import json


class Tournament:
    def __init__(self, name, place, start_date, end_date,
                 actual_round, list_of_player, description, list_of_round=4):
        self.name = name
        self.place = place
        self.start_date = start_date
        self.end_date = end_date
        self.actual_round = actual_round
        self.list_of_player = list_of_player
        self.list_of_round = list_of_round
        self.description = description

    def __str__(self):
        return f"Bienvenue au tournoi {self.name}, qui a lieu a {self.place}"

    def create_tournament(self):
        tournament = {"name": self.name, "place": self.place,
                      "start_date": self.start_date, "end_date": self.end_date}
        tournament_data = json.dumps(tournament, indent=2)
        with open("data/tournaments.json", "a") as f:
            f.write(tournament_data)

    def add_players():
        print("Inscrire les participants")

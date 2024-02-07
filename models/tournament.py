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

    def create_tournament():
        print("Souhaitez vous créer un nouveau tournoi?")
        choice = input("Oui (O) / Non (N) ?")
        if choice == "O":
            print("Informations du nouveau tournoi:")
            name = input("Nom du tournoi:")
            place = input("Lieu: ")
            dates = input("Dates: ")

            tournament = {
                "name": name,
                "place": place,
                "dates": dates
            }
            tournament_data = json.dumps(tournament, indent=2)
            with open("data/tournaments.json", "a") as f:
                f.write(tournament_data)
        elif choice == "N":
            print("")
        else:
            print("Je n'ai pas compris votre réponse")

    def add_players():
        print("Inscrire les participants")

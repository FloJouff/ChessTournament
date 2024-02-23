import json
from datetime import datetime
import uuid


class Tournament:
    def __init__(self, name, place, start_date, end_date, description,
                 number_of_round=4, id=uuid.uuid4()):
        self.name = name
        self.place = place
        self.start_date = start_date
        self.end_date = end_date
        self.description = description
        self.number_of_round = number_of_round
        self.id = id
        self.players = []
        self.rounds = []

    def __str__(self):
        return f"Bienvenue au tournoi {self.name}, a {self.place}"

    def to_dict(self):
        return {"id": str(self.id), "name": self.name, "place": self.place,
                "start_date": self.start_date, "end_date": self.end_date,
                "number_of_round": self.number_of_round,
                "players": self.players, "description": self.description,
                "Rounds": [round.to_dict() for round in self.rounds]
                }

    def create_tournament(self):
        with open("data/tournaments.json", "r") as f:
            data = json.load(f)
        tournament_data = self.to_dict()
        data.append(tournament_data)
        with open("data/tournaments.json", "w") as f:
            json.dump(data, f, indent=4)

    def display_tournaments():
        with open("data/tournaments.json", "r") as f:
            data = json.loads(f.read())
            print(data)

    def load_tournament_by_id(id):
        tournament = None
        with open("data/tournaments.json", "r") as f:
            data = json.load(f)
            for tournament_dict in data:
                if tournament_dict['id'] == id:
                    tournament = Tournament(tournament_dict["name"],
                                            tournament_dict["place"],
                                            tournament_dict["start_date"],
                                            tournament_dict["end_date"],
                                            tournament_dict["number_of_round"],
                                            tournament_dict["players"],
                                            tournament_dict["id"],)
                    break
        return tournament


class Round:
    def __init__(self, round_nb, matches, start_time, end_time=""):
        self.round_nb = round_nb
        self.matches = matches
        self.start_time = start_time
        self.end_time = end_time

    def to_dict(self):
        return {"Round": self.round_nb, "matchs": self.matches,
                "start_time": self.start_time,
                "end_time": self.end_time
                }

# incription de l'heure du début du tour.

    def creation_round():
        print("Début d'un nouveau tour")
        round_start = datetime.now()
        print("")
        print("Heure de début du tour : ", round_start)
        print("")
        return round_start

# incription de l'heure du fin du tour.

    def round_closure(self):
        print("Fin du tour")
        round_end = datetime.now()
        print("")
        print("Le tour en cours s'est terminé à :", round_end)
        print("")
        return round_end

    def save_round(self, id):
        with open("data/tournaments.json", "r") as f:
            data = json.load(f)
        # L'id de l'élément que vous souhaitez mettre à jour
        element_id = id

        # Rechercher l'élément avec l'id spécifié
        element_a_mettre_a_jour = next((element for element in data if element["id"] == element_id), None)

        if element_a_mettre_a_jour:

            element_a_mettre_a_jour["Rounds"].append({
                "round_nb": self.round_nb,
                "round_matches": self.matches,
                "round_start_time": self.start_time

            })

            # Enregistrer les modifications dans le fichier JSON
            with open('votre_fichier.json', 'w') as fichier:
                json.dump(data, fichier, indent=2)
        else:
            print(f"Aucun élément trouvé avec l'id {element_id}")

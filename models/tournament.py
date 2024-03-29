from datetime import datetime
import uuid
import json


class Tournament:
    def __init__(self, name, place, start_date, end_date, description, number_of_round=4, id=uuid.uuid4()):
        """Constructor of tournament's object

        Args:
            name (str): tournament's name
            place (str): tournament's place
            start_date (str): tournament's start date
            end_date (str): tournament's end date
            description (str): tournament's description
            number_of_round (int, optional): _description_. Defaults to 4.
            id (str, optional): _description_. Defaults to uuid.uuid4().
        """
        self.name = name
        self.place = place
        self.start_date = start_date
        self.end_date = end_date
        self.description = description
        self.number_of_round = number_of_round
        self.id = id
        self.players = []
        self.rounds = []
        self.status = "tostart"

    def __str__(self):
        return f"Bienvenue au tournoi {self.name}, qui se déroule à {self.place}"

    def to_dict(self):
        return {
            "id": str(self.id),
            "name": self.name,
            "place": self.place,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "number_of_round": self.number_of_round,
            "players": self.players,
            "description": self.description,
            "rounds": [round.to_dict() for round in self.rounds],
            "status": self.status,
        }

    def create_tournament(self):
        """Create new tournament in json"""
        with open("data/tournaments.json", "r") as f:
            data = json.load(f)
        tournament_data = self.to_dict()
        data.append(tournament_data)
        with open("data/tournaments.json", "w") as f:
            json.dump(data, f, indent=2)

    @staticmethod
    def load_tournament_by_id(id):
        """Load tournament by id

        Args:
            id (str): tournament's id

        Returns:
            tournament(object): tournament's instance
        """
        tournament = None
        with open("data/tournaments.json", "r") as f:
            data = json.load(f)
            for tournament_dict in data:
                if tournament_dict["id"] == id:
                    tournament = Tournament(
                        tournament_dict["name"],
                        tournament_dict["place"],
                        tournament_dict["start_date"],
                        tournament_dict["end_date"],
                        tournament_dict["number_of_round"],
                        tournament_dict["players"],
                        tournament_dict["id"],
                    )
                    break
        return tournament

    @staticmethod
    def change_status_start_inprogress(id):
        """Change tournament's status from tostart to inprogress

        Args:
            id (str): round's id
        """
        with open("data/tournaments.json", "r") as f:
            data = json.load(f)
        tournoi = None
        for d in data:
            if d["id"] == str(id):
                tournoi = d
        if tournoi:
            tournoi["status"] = str("inprogress")
            with open("data/tournaments.json", "w") as fichier:
                json.dump(data, fichier, indent=2)
        else:
            print(f"Aucun élément trouvé avec l'id {id}")

    @staticmethod
    def close_tournament(id):
        """Change tournament's status to done

        Args:
            id (str): round's id
        """
        with open("data/tournaments.json", "r") as f:
            data = json.load(f)
        tournoi = None
        for d in data:
            if d["id"] == str(id):
                tournoi = d
        if tournoi:
            tournoi["status"] = str("done")
            with open("data/tournaments.json", "w") as fichier:
                json.dump(data, fichier, indent=2)
        else:
            print(f"Aucun élément trouvé avec l'id {id}")


class Round:
    def __init__(self, round_nb, matches, start_time="", end_time=""):
        """Constructor of object round

        Args:
            round_nb (int): _description_
            matches (list): _description_
            start_time (str, optional): beginning of round. Defaults to "".
            end_time (str, optional): end of round. Defaults to "".
        """
        self.round_nb = round_nb
        self.start_time = start_time
        self.matches = matches
        self.end_time = end_time

    def to_dict(self):
        matchs_json = []
        for m in self.matches:
            matchs_json.append(([m[0][0].id, m[0][1]], [m[1][0].id, m[1][1]]))
        return {
            "round": self.round_nb,
            "start_date": str(self.start_time),
            "matchs": matchs_json,
            "end_date": str(self.end_time),
        }

    def creation_round(self):
        """Records start date

        Returns:
            round_start(datetime): beginning of turn
        """
        print("Début d'un nouveau tour")
        round_start = datetime.now()
        print("")
        print("Heure de début du tour : ", round_start)
        print("")
        return round_start

    def round_closure(self):
        """Records end date

        Returns:
            round_end(datetime): end of turn
        """
        round_end = datetime.now()
        print("")
        print("Ce tour s'est terminé à :", round_end)
        print("")
        return round_end

    def save_round(self, id):
        """Save round on json file

        Args:
            id (str): tournament's id
        """
        with open("data/tournaments.json", "r") as fichier:
            data = json.load(fichier)
        # Rechercher l'élément avec l'id spécifiée
        tournoi = None
        for d in data:
            if d["id"] == str(id):
                tournoi = d
        if tournoi:
            # Ajouter de nouvelles informations à la section "Rounds"
            tournoi["rounds"].append(self.to_dict())
            with open("data/tournaments.json", "w") as fichier:
                json.dump(data, fichier, indent=2)
        else:
            print(f"Aucun élément trouvé avec l'id {id}")

import json
import uuid
# from serializer import Serializer


class Player:
    def __init__(self, name, first_name, gender, date_of_birth, ine,
                 id=uuid.uuid4()):
        self.name = name
        self.first_name = first_name
        self.gender = gender
        self.date_of_birth = date_of_birth
        self.id = id
        self.ine = ine
        self.score = 0.0

    def __str__(self):
        return f"Nom et prénom du joueur: {self.name}, {self.first_name}"

    def __repr__(self):
        return str(self)

    def to_dict(self):
        return {"id": str(self.id), "name": self.name,
                "first_name": self.first_name,
                "gender": self.gender, "date_of_birth": self.date_of_birth,
                "ine": self.ine}

    def save(self):
        with open("data/player_data.json", "r") as f:
            data = json.load(f)
        player_data = self.to_dict()
        data.append(player_data)
        with open("data/player_data.json", "w") as f:
            json.dump(data, f, indent=4)

    def load_all_players():
        player_list = []
        with open("data/player_data.json", "r") as f:
            data = json.load(f)
            for player_dict in data:
                p = Player(player_dict["name"],
                           player_dict["first_name"],
                           player_dict["gender"], player_dict["date_of_birth"],
                           player_dict["ine"], player_dict["id"])
                player_list.append(p)
        return player_list

    def load_player_by_id(id):
        player = None
        with open("data/player_data.json", "r") as f:
            data = json.load(f)
            for player_dict in data:
                if player_dict['id'] == id:
                    player = Player(player_dict["name"],
                                    player_dict["first_name"],
                                    player_dict["gender"],
                                    player_dict["date_of_birth"],
                                    player_dict["id"], 
                                    player_dict["ine"])
                    break
        return player

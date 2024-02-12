import json
# from serializer import Serializer


class Player:
    def __init__(self, name, first_name, gender, date_of_birth):
        self.name = name
        self.first_name = first_name
        self.gender = gender
        self.date_of_birth = date_of_birth
        self.INE = str
        self.score = 0.0

    def __str__(self):
        return f"Nom et prénom du joueur: {self.name}, {self.first_name}"

    def __repr__(self):
        return self.name, self.first_name

    def to_dict(self):
        return {"name": self.name, "first_name": self.first_name,
                "gender": self.gender, "date_of_birth": self.date_of_birth}

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
            # for line in f:
            #     player_list.append(json.loads(line))
            data = json.load(f)
            # c une liste de dictionnaire de player
            # list de objet player
            for player_dict in data:
                p = Player(player_dict["name"], player_dict["first_name"],
                           player_dict["gender"], player_dict["date_of_birth"])
                p.name = player_dict["name"]
                p.first_name = player_dict["first_name"]
                p.gender = player_dict["gender"]
                p.date_of_birth = player_dict["date_of_birth"]
                player_list.append(p)
        return player_list

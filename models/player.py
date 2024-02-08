import json
# from serializer import Serializer


class Player:
    def __init__(self, name, surname, gender, date_of_birth):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.date_of_birth = date_of_birth
        self.INE = str
        self.score = 0.0

    def __str__(self):
        return f"{self.name}, {self.surname}"

    def __repr__(self):
        return f"({self.name}, {self.surname})"

    def to_dict(self,):
        return {"name": self.name, "surname": self.surname,
                "gender": self.gender, "date_of_birth": self.date_of_birth}

    def save(self):
        player_data = json.dumps(self.to_dict(), indent=4)
        with open("data/player_data.json", "a") as f:
            f.write(player_data)

    def load_one_player_from_json():
        with open("data/player_data.json", "r") as f:
            data = json.load(f)

        choice = input("Nom du joueur recherché:")

        for player in data["players"]:
            if player['name'] == choice:
                print("Nom du joueur: ", player['name'])
                print("Prénom du joueur: ", player['surname'])
                print("Sexe du joueur: ", player['gender'])
                print("Date de naissance du joueur: ", player['date_of_birth'])

    def load_all_players():
        player_list = []
        with open("data/player_data.json", "r") as f:
            data = json.load(f)
            # c unelsite dictionnaire de player
            # list de objet player
            for player_dict in data:
                p = Player()
                p.name = player_dict["name"]
                p.surname = player_dict["surname"]
                p.gender = player_dict["gender"]
                p.name = player_dict["name"]
                player_list.append(p)
        return player_list

import json
import uuid
import re


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
        return f"{self.name} {self.first_name}"

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

    def load_player_by_ine(ine):
        player = None
        with open("data/player_data.json", "r") as f:
            data = json.load(f)
            for player_dict in data:
                if player_dict['ine'] == ine:
                    player = Player(player_dict["name"],
                                    player_dict["first_name"],
                                    player_dict["gender"],
                                    player_dict["date_of_birth"],
                                    player_dict["id"],
                                    player_dict["ine"])
                    break
        return player

    def ine_validation(new_ine):
        # Verification que l'INE indiqué n'existe pas déjà:
        with open("data/player_data.json", "r") as f:
            data = json.load(f)

            if any(element.get('ine') == new_ine for element in data):
                print(f"Cet INE {new_ine} existe déjà dans le fichier json")
                return False

        # Vérification que le format de l'INE est correct:
        pattern = re.compile(r"^[A-Za-z]{2}\d{5}$")

        if pattern.match(new_ine):
            return True
        else:
            print("Format invalide. Utilisez 2 lettres suivies de 5 chiffres.")
            return False

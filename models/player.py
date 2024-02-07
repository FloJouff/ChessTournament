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

    def create_player():
        print("Souhaitez vous enregistrer un nouveau joueur?")
        choice = input("Oui (O) / Non (N) ?")
        if choice == "O":
            print("Enregistrer un nouveau joueur:")
            name = input("Nom du joueur:")
            surname = input("Prénom: ")
            gender = input("Sexe: ")
            date_of_birth = input("Date de naissance: ")
            player = {
                "name": name,
                "surname": surname,
                "gender": gender,
                "date_of_birth": date_of_birth,
            }
            player_data = json.dumps(player, indent=4)
            with open("data/player_data.json", "a") as f:
                f.write(player_data)
        elif choice == "N":
            print("")
        else:
            print("Je n'ai pas compris votre réponse")

    def load_one_player_from_json():
        with open("data/player_data.json", "r") as f:
            data = json.load(f)

        print("Chargement des données d'un joueur")
        choice = input("Nom du joueur recherché:")

        for player in data["players"]:
            if player['name'] == choice:
                print("Nom du joueur: ", player['name'])
                print("Prénom du joueur: ", player['surname'])
                print("Sexe du joueur: ", player['gender'])
                print("Date de naissance du joueur: ", player['date_of_birth'])

    def load_all_players():
        with open("data/player_data.json", "r") as f:
            data = json.load(f)

        print("Liste des joueurs: ")
        for player in data["players"]:
            print(player['name'], player['surname'])


player1 = Player("Maximoff", "Wanda", "F", "01/03/1964")
player1.score = 0.0

player2 = Player("Stark", "Tony", "M", "28/03/1963")
player2.score = 0.5

player3 = Player("Rogers", "Steve", "M", "01/03/1940")
player3.score = 0.0

player4 = Player("Danvers", "carol", "F", "10/03/1968")
player4.score = 1.0

player5 = Player("Parker", "Peter", "M", "15/08/1962")
player5.score = 2.0

player6 = Player("Xavier", "Charles", "M", "12/09/1963")
player6.score = 10.0

player7 = Player("Lensher", "Eric", "M", "25/09/1963")
player7.score = 0.5

player8 = Player("Howlett", "James", "M", "11/10/1974")
player8.score = 2.5


player_list = [player1, player2, player3, player4, player5, player6,
               player7, player8]

scores_list = [
    player1.score,
    player2.score,
    player3.score,
    player4.score,
    player5.score,
    player6.score,
    player7.score,
    player8.score,
]

print(scores_list)
# scores_list.sort()
# print(scores_list)

# serializer = Serializer[Player]()
# Player.load_one_player_from_json()
# print(tournament_player_list)
Player.create_player()

# Player.load_all_players()

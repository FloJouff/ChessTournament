from models.tournament import Tournament
from models.player import Player
import json
import os
import csv


class Report:
    def add_data_to_csv(file_name, fieldnames, data):
        os.makedirs("fichiers_csv", exist_ok=True)
        if os.path.isfile("fichiers_csv" + "//" + f"{file_name}.csv"):
            with open("fichiers_csv" + "//" + f"{file_name}.csv", "a", encoding="UTF-8-sig") as fichier_csv:
                writer = csv.writer(fichier_csv, delimiter=",", lineterminator="\n")
                writer.writerow(data)
        else:
            fieldname = fieldnames
            with open("fichiers_csv" + "//" + f"{file_name}.csv", "a", encoding="UTF-8-sig") as fichier_csv:
                writer = csv.writer(fichier_csv, delimiter=",", lineterminator="\n")
                writer.writerow(fieldname)
                writer.writerow(data)

    def all_players_list_report(self):
        with open("data/player_data.json", "r") as f:
            data = json.loads(f.read())
            print(data)

    def display_tournaments(self):
        with open("data/tournaments.json", "r") as f:
            data = json.loads(f.read())

        tournament = []
        for d in data:
            tournament.append(d)
        print("")
        i = 0
        for t in tournament:
            print(
                i,
                "Nom: ",
                t["name"],
                "   Lieu: ",
                t["place"],
                "   Date de début: ",
                t["start_date"],
                "   Date de fin: ",
                t["end_date"],
                "   Description: ",
                t["description"],
                "   statut: ",
                t["status"],
            )
            i = i + 1
        return data

    def load_tournament_by_id(id):
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
                        tournament_dict["description"],
                        tournament_dict["players"],
                        tournament_dict["rounds"],
                    )
                    break
        return tournament

    def get_tournament_participants_by_id(id):
        tournament = None
        with open("data/tournaments.json", "r") as f:
            data = json.load(f)
            for tournament_dict in data:
                if tournament_dict["id"] == id:
                    tournament = tournament_dict["players"]
                    break
        return tournament

    def get_tournament_numb_of_round_by_id(id):
        tournament = None
        with open("data/tournaments.json", "r") as f:
            data = json.load(f)
            for tournament_dict in data:
                if tournament_dict["id"] == id:
                    tournament = tournament_dict["number_of_round"]
                    break
        return tournament

    def display_matches_per_round(id, round_nb):
        tournament = None
        with open("data/tournaments.json", "r") as f:
            data = json.load(f)
            for tournament_dict in data:
                if tournament_dict["id"] == id:
                    for round_dict in tournament_dict["rounds"]:
                        if round_dict["round"] == int(round_nb):
                            print(f"Matchs du tour {round_nb}:", round_dict["matchs"])
                            for i in range(0, int(len(round_dict["matchs"]))):
                                for j in range(0, 2):
                                    joueur = Player.load_player_by_id(round_dict["matchs"][i][j][0])
                                    round_dict["matchs"][i][j][0] = joueur
                                    tournament = round_dict["matchs"]
                            break
        return tournament

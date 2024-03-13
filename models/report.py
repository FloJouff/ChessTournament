from models.tournament import Tournament
from models.player import Player
import json
import os
import csv


class Report:
    def add_data_to_csv(file_name, fieldnames, data):
        """Add datas to csv file

        Args:
            file_name (str)
            fieldnames (str)
            data (list)
        """
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
        """Display all players recorded on json file"""
        with open("data/player_data.json", "r") as f:
            data = json.loads(f.read())
            print(data)

    def display_tournaments(self):
        """Display list of tournaments recorded on json file

        Returns:
            list: _description_
        """
        with open("data/tournaments.json", "r") as f:
            data = json.loads(f.read())
        tournament = []
        for d in data:
            tournament.append(d)
        print("")
        i = 1
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
        """Load a tournament by his id

        Args:
            id (str): tournament's id

        Returns:
            object tournament
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
                        tournament_dict["description"],
                        tournament_dict["players"],
                        tournament_dict["rounds"],
                    )
                    break
        return tournament

    def get_tournament_participants_by_id(id):
        """Get a tournament's list of players

        Args:
            id (str): tournament's id

        Returns:
            list of players
        """
        tournament = None
        with open("data/tournaments.json", "r") as f:
            data = json.load(f)
            for tournament_dict in data:
                if tournament_dict["id"] == id:
                    tournament = tournament_dict["players"]
                    break
        return tournament

    def get_tournament_numb_of_round_by_id(id):
        """Get the number of round for a turnament

        Args:
            id (str): tournament's id

        Returns:
            number_of_round(int)
        """
        tournament = None
        with open("data/tournaments.json", "r") as f:
            data = json.load(f)
            for tournament_dict in data:
                if tournament_dict["id"] == id:
                    tournament = tournament_dict["number_of_round"]
                    break
        return tournament

    def display_matches_per_round(id, round_nb):
        """display list of matchs per round

        Args:
            id (str): tournament's id
            round_nb (int): round of the number

        Returns:
            matchs(list): list of matchs
        """
        tournament = None
        with open("data/tournaments.json", "r") as f:
            data = json.load(f)
            for tournament_dict in data:
                if tournament_dict["id"] == id:
                    for round_dict in tournament_dict["rounds"]:
                        if round_dict["round"] == int(round_nb):
                            for i in range(0, int(len(round_dict["matchs"]))):
                                for j in range(0, 2):
                                    joueur = Player.load_player_by_id(round_dict["matchs"][i][j][0])
                                    round_dict["matchs"][i][j][0] = joueur
                                    tournament = round_dict["matchs"]
                            print(f"Matchs du tour {round_nb}:", round_dict["matchs"])
                            break
        return tournament

    def display_rounds_matchs(id):
        """display list of matchs for all rounds of a turnament

        Args:
            id (str): tournament's id

        Returns:
            round_list(list): list of matchs for all rounds
        """
        tournament = None
        round_list = []
        with open("data/tournaments.json", "r") as f:
            data = json.load(f)
            for tournament_dict in data:
                if tournament_dict["id"] == id:
                    print(f"Tournoi {tournament_dict["name"]}")
                    for round_dict in tournament_dict["rounds"]:
                        for i in range(0, int(len(round_dict["matchs"]))):
                            for j in range(0, 2):
                                joueur = Player.load_player_by_id(round_dict["matchs"][i][j][0])
                                round_dict["matchs"][i][j][0] = joueur
                            tournament = [round_dict["round"], round_dict["matchs"]]
                        round_list.append(tournament)
                        print("Tour:", round_dict["round"])
                        print("Matchs :")
                        for match in round_dict["matchs"]:
                            print(match[0], "vs", match[1])
                    break
        return round_list

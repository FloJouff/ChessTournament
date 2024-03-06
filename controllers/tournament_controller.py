from views.tournament_view import TournamentView, MatchView
from models.tournament import Tournament, Round
from models.player import Player
from models.report import Report
from views.player_view import PlayerView
import Constantes.constantes as constante
import random
import json

matchs_played = []


class TournamentController:
    def __init__(self) -> None:
        self.tournamentview = TournamentView()
        self.playerviews = PlayerView()

    def run_tournament(self):
        choix = ""
        while choix != "0":
            choix = self.tournamentview.menu_tournoi()
            if choix == constante.CREATE_TOURNAMENT:
                data = self.tournamentview.get_tournament_infos()
                print(data)
                tournoi = Tournament(
                    data["name"],
                    data["place"],
                    data["start_date"],
                    data["end_date"],
                    data["description"],
                    data["number_of_round"]
                )
                print("Ajouter les joueurs au tournoi")
                self.generate_list_of_player(tournoi)
                tournoi.create_tournament()
            elif choix == constante.DISPLAY_TOURNAMENTS:
                Report.display_tournaments(self)
            elif choix == constante.START_NEW_TOURNAMENT:
                tournoi = self.load_tournament_start()
                matches = self.round1_generating_matches(tournoi)
                for i in range(1, int(tournoi["number_of_round"]) + 1):
                    start_time = str(Round.creation_round(self))
                    round = Round(i, matches, start_time)
                    print("debut", start_time)
                    print(f"Liste des matchs du tour {i}:")
                    print("")
                    print("Matchs: ", round.matches)
                    print("")
                    print(f"Saisissez les résultats de match du tour{i}")
                    players_and_score = self.match_resolution(round.matches)
                    self.check_played_matchs(round.matches)
                    matches = self.score_based_generating_matches(players_and_score)
                    round.end_time = round.round_closure()
                    print(f"Fin du tour {i}")
                    id = str(tournoi["id"])
                    Tournament.change_status_start_inprogress(id)
                    round.save_round(tournoi["id"])
                    print("")
                print(f"le vainqueur du tournoi {tournoi["name"]} est {players_and_score[0]}")
                id = str(tournoi["id"])
                Tournament.close_tournament(id)
            elif choix == constante.RESUME_TOURNAMENT:
                tournoi = self.load_tournament_inprogress()
                last_round_played = int(tournoi["rounds"][-1]["round"])
                matches = Report.display_matches_per_round(tournoi["id"], last_round_played)
                for i in range(last_round_played + 1, int(tournoi["number_of_round"]) + 1):
                    start_time = str(Round.creation_round(self))
                    round = Round(i, matches, start_time)
                    print("debut", start_time)
                    print(f"Liste des matchs du tour {i}:")
                    print("")
                    print("Matchs : ", round.matches)
                    print("")
                    print(f"Saisissez les résultats de match du tour{i}")
                    players_and_score = self.match_resolution(round.matches)
                    self.check_played_matchs(round.matches)
                    matches = self.score_based_generating_matches(players_and_score)
                    round.end_time = round.round_closure()
                    print(f"Fin du tour {i}")
                    round.save_round(tournoi["id"])
                    print("")
                print(f"le vainqueur du tournoi {tournoi["name"]} est {players_and_score[0]}")
                print("")
                id = str(tournoi["id"])
                Tournament.close_tournament(id)
            elif choix == "0":
                print("Quitter")
                break

    def generate_list_of_player(self, tournoi):
        players = Player.load_all_players(self)
        self.playerviews.display_list_players(players)
        nb_participants = input("Indiquez le nombre de participants à ce tournoi: ")
        while (len(tournoi.players) < int(nb_participants)):
            choix = input("Saissez le numéro du joueur à inclure dans le tournoi: ")
            id_player = players[int(choix)].id
            if id_player not in tournoi.players:
                tournoi.players.append(id_player)
            else:
                print("Ce joueur est déjà inscrit à ce tournoi")
                return False
        return players

    def display_list_participants_with_score(self, tournoi):
        players = tournoi["players"]
        players_name = [Player.load_player_by_id(player) for player in players]
        scores = {player: 0.0 for player in players_name}
        players_and_score = [[player, scores[player]] for player in players_name]
        return players_and_score

    def check_played_matchs(self, matchs):
        if matchs in matchs_played:
            return True
        else:
            matchs_played.append(matchs)
            return False

# Création d'une liste aléatoire, sans répétition, de tous les participants
# pour le premier tour uniquement

    def round1_generating_matches(self, tournoi):
        players_and_score = self.display_list_participants_with_score(tournoi)
        matches1 = []
        while len(players_and_score) >= 2:
            joueur1 = random.choice(players_and_score)
            players_and_score.remove(joueur1)
            joueur2 = random.choice(players_and_score)
            players_and_score.remove(joueur2)
            matches1.append((joueur1, joueur2))
        for match in matches1:
            print(match)
        return matches1

    def match_resolution(self, matches):
        for match in matches:
            print("-------------------------------------------")
            MatchView.display_match(match[0], match[1])
            MatchView.match_results_entry(match[0], match[1])
        print("")
        print("Nouvelle liste de joueurs avec les scores à jour: ")
        print("")
        players_and_score = []
        for match in matches:
            for joueur in match:
                players_and_score.append(joueur)
                print(joueur)
        print("")
        return players_and_score

    def score_based_generating_matches(self, players_and_score):
        random.shuffle(players_and_score)
        players_and_score.sort(key=lambda x: x[1], reverse=True)
        print("Liste des joueurs par ordre décroissant de score: ",
              players_and_score)
        print("")
        matches = []
        for i in range(0, len(players_and_score), 2):
            if i + 1 < len(players_and_score):
                joueur1 = players_and_score[i]
                if ((players_and_score[i], players_and_score[i + 1]) in matchs_played) or ((players_and_score[i + 1], players_and_score[i]) in matchs_played):
                    temp = players_and_score[i + 1]
                    players_and_score[i + 1] = players_and_score[i + 2]
                    players_and_score[i + 2] = temp
                joueur2 = players_and_score[i + 1]
            matches.append((joueur1, joueur2))
        return matches

    def load_tournament_inprogress(self):
        with open("data/tournaments.json", "r") as f:

            data = json.load(f)
        tournoi = []
        for d in data:
            if d["status"] == str("inprogress"):
                tournoi.append(d)
        print("Afficher tous les tournois en cours: ")
        i = 0
        for t in tournoi:
            print(i, t["name"], t["place"], t["status"])
            i = i + 1
        choix = input("Saissez le numéro du tournoi à reprendre: ")
        tournoi = tournoi[int(choix)]
        return tournoi

    def load_tournament_start(self):
        with open("data/tournaments.json", "r") as f:
            data = json.load(f)
        tournament = []
        for d in data:
            if d["status"] == str("tostart"):
                tournament.append(d)
        print("Afficher tous les tournois non démarrés: ")
        i = 0
        for t in tournament:
            print(i, t["name"], t["place"], t["status"])
            i = i + 1
        choix = input("Saissez le numéro du tournoi à démarrer: ")
        tournoi = tournament[int(choix)]
        return tournoi

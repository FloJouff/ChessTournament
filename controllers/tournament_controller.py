from views.tournament_view import TournamentView, MatchView
from models.tournament import Tournament, Round
from models.player import Player
import random
from views.player_view import PlayerView


class TournamentController:
    def __init__(self) -> None:
        self.tournamentview = TournamentView()
        self.playerviews = PlayerView()

    def run_tournament(self):
        choix = ""
        while choix != "0":
            choix = self.tournamentview.menu_tournoi()
            if choix == "1":
                data = self.tournamentview.get_tournament_infos()
                print(data)
                tournoi = Tournament(
                    data["name"],
                    data["place"],
                    data["start_date"],
                    data["end_date"],
                    data["nombre_de_tour"]
                )
                print("Ajouter les joueurs au tournoi")
                self.generate_list_of_player(tournoi)
                tournoi.create_tournament()
            elif choix == "2":
                print(tournoi.players)
            elif choix == "3":
                round_nb = input("Veuillez préciser le numéro du tour: ")
                round = Round(round_nb)
                round.creation_round()
                print(f"Liste des matchs du tour {round_nb}:")
                if round_nb == "1":
                    matches1 = self.round1_generating_matches(tournoi)
                elif round_nb == "2":
                    matches = self.score_based_generating_matches(players_and_score1)
                else:
                    matches = self.score_based_generating_matches(players_and_score)
            elif choix == "4":
                if round_nb == "1":
                    print("Saisissez les résultats de match du tour 1")
                    players_and_score1 = self.round1_match_resolution(matches1)
                else:
                    print(f"Saisissez les résultats de match du tour {round_nb}")
                    players_and_score = self.next_round_match_resolution(matches)
            elif choix == "5":
                Round.round_closure(self)
                print(f"Fin du tour {round_nb}")
            elif choix == "6":
                TournamentView.get_description(self)
            elif choix == "0":
                print("Quitter")
                break

    def generate_list_of_player(self, tournoi):
        players = Player.load_all_players()
        self.playerviews.display_list_players(players)
        while (len(tournoi.players) < 6):
            choix = input("Saissez le numéro du joueur à inclure dans le tournoi: ")
            id_player = players[int(choix)].name                    # name au lieu de id, pas plus clair????
            tournoi.players.append(id_player)
        return players

    def display_list_participants_with_score(self, tournoi):
        players = tournoi.players
        scores = {player: 0.0 for player in players}
        players_and_score = [[player, scores[player]] for player in players]

        return players_and_score

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
            matches1.append([joueur1, joueur2])
        for match in matches1:
            print(match)

        return matches1

    def round1_match_resolution(self, matches1):
        for player in matches1:
            print("-------------------------------------------")
            MatchView.display_match(player[0], player[1])
            MatchView.match_results_entry(player[0], player[1])
        print("")
        print("Nouvelle liste de joueurs avec les scores à jour: ")
        print("")

        players_and_score = []
        for player in matches1:
            for joueur in player:
                players_and_score.append(joueur)
                print(joueur)
        print("")

        players_and_score.sort(key=lambda x: x[1], reverse=True)
        print(players_and_score)
        print("")

        return players_and_score

    def score_based_generating_matches(self, players_and_score):

        print("Liste des joueurs par ordre décroissant de score: ",
              players_and_score)
        print("")

        matches = []
        for i in range(0, len(players_and_score), 2):
            if i + 1 < len(players_and_score):
                joueur1 = players_and_score[i]
                joueur2 = players_and_score[i + 1]
            matches.append([joueur1, joueur2])
        print(matches)

        return matches

    def next_round_match_resolution(self, matches):
        for player in matches:
            print("-------------------------------------------")
            MatchView.display_match(player[0], player[1])
            MatchView.match_results_entry(player[0], player[1])
        print("Nouvelle liste de joueurs avec les scores à jour: ")

        players_and_score = []
        for player in matches:
            for joueur in player:
                players_and_score.append(joueur)
                print(joueur)
        players_and_score.sort(key=lambda x: x[1], reverse=True)
        print(players_and_score)
        return players_and_score

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
                    data["description"],
                    data["number_of_round"]
                )
                print("Ajouter les joueurs au tournoi")
                self.generate_list_of_player(tournoi)
                tournoi.create_tournament()
            elif choix == "2":
                liste = Tournament.display_tournaments()
                print(liste)
            elif choix == "3":
                id = input("Veuillez saisir l'id du tournoi souhaité: ")
                tournoi = Tournament.load_tournament_by_id(id)
                print(tournoi)
            elif choix == "4":
                matches = self.round1_generating_matches(tournoi)
                for i in range(1, int(tournoi.number_of_round)+1):
                    round_start = str(Round.creation_round())
                    round = Round(i, matches, round_start)
                    print(f"Liste des matchs du tour {i}:")
                    print("")
                    round.save_round(tournoi.id)
                    print(matches)
                    print(f"Saisissez les résultats de match du tour{i}")
                    players_and_score1 = self.match_resolution(matches)
                    matches = self.score_based_generating_matches(players_and_score1)
                    round.round_closure()
                    print(f"Fin du tour {i}")
                    print("")             
                print(f"le vainqueur du tournoi {tournoi.name} est {players_and_score1[0]}")
            elif choix == "5":
                pass
            elif choix == "0":
                print("Quitter")
                break

    def generate_list_of_player(self, tournoi):
        players = Player.load_all_players()
        self.playerviews.display_list_players(players)
        nb_participants = input("Indiquez le nombre de participants à ce tournoi: ")
        while (len(tournoi.players) < int(nb_participants)):
            choix = input("Saissez le numéro du joueur à inclure dans le tournoi: ")
            id_player = players[int(choix)].id
            tournoi.players.append(id_player)
        return players

    def display_list_participants_with_score(self, tournoi):
        players = tournoi.players
        players_name = [Player.load_player_by_id(player) for player in players]

        scores = {player: 0.0 for player in players_name}
        players_and_score = [[player, scores[player]] for player in players_name]

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

    def match_resolution(self, matches):
        for player in matches:
            print("-------------------------------------------")
            MatchView.display_match(player[0], player[1])
            MatchView.match_results_entry(player[0], player[1])
        print("")
        print("Nouvelle liste de joueurs avec les scores à jour: ")
        print("")

        players_and_score = []
        for player in matches:
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
                # si [joueur[i], joueur[i+1]] existe déjà alors créer [joueur[i], joueur[i+2]]
            matches.append([joueur1, joueur2])
        print(matches)

        return matches

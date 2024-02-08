from views.tournament_view import TournamentView, RoundView, MatchView
from models.tournament import Tournament
from models.player import Player
import random
import copy


class TournamentController:
    def __init__(self) -> None:
        self.tournamentview = TournamentView()

    def run_tournament(self,):
        choix = ""
        while choix != "0":
            choix = self.tournamentview.menu_tournoi()
            if choix == "1":
                data = self.tournamentview.get_tournament_infos()
                print(data)
                tournoi = Tournament(data["name"],
                                     data["place"], data["dates"])
                tournoi.save()
            elif choix == "2":
                TournamentView.register_player()
            elif choix == "3":
                self.add_tournament_players()
            elif choix == "4":
                data["description"] = input(
                    "Veuillez rentrer une description pour ce tournoi: "
                )
            elif choix == "0":
                print("Quitter")
                break

    def add_tournament_players(self):
        Tournament.players.append(Player.name)
        Player.score = 0.0
        new_list = [(nom, Player.score) for nom in Tournament.players]
        for tuple in new_list:
            print(tuple)
        return new_list

    def round_management():
        pass


class RoundController:
    def __init__(self) -> None:
        self.roundview = RoundView()

    def run_round(self):
        choix = ""
        while (choix != "0"):
            choix = self.roundview.round_menu()
            if choix == "1":
                RoundController.round1_generating_matches()
            elif choix == "2":
                RoundController.score_based_generating_matches()
            elif choix == "0":
                print("Quitter")
                break

# Création d'une liste aléatoire, sans répétition, de tous les joueurs inscrits

    def round1_generating_matches(self):
        random.shuffle(Tournament.player_list)
        player_list2 = copy.deepcopy(Tournament.player_list)

        if len(Tournament.player_list) % 2 != 0:
            raise ValueError

        print("Liste des matchs du 1er tour:")

        match = [(player_list2[i], player_list2[i + 1])
                 for i in range(0, len(player_list2), 2)]
        for paire in match:
            player_list2.remove(paire[0])
            player_list2.remove(paire[1])

        print(match)

# Création d'une liste de matchs,
# en fonction du score à l'issue des tours précédents:

    def score_based_generating_matches(self):
        based_score_list = sorted(Tournament.new_list,
                                  key=lambda x: x[1], reverse=True)
        print("Liste des joueurs par ordre décroissant de score: ",
              based_score_list)
        for nom, score in based_score_list:
            print(nom, score)

        if len(based_score_list) % 2 != 0:
            raise ValueError

        print("Liste des matchs du tour:")

        match = [(based_score_list[i], based_score_list[i + 1])

                 for i in range(0, len(based_score_list), 2)]
        for paire in match:
            based_score_list.remove(paire[0])
            based_score_list.remove(paire[1])

        print(match)


class MatchController:
    def __init__(self) -> None:
        self.matchview = MatchView()

    def match_progress(player1, player2):
        match_result = random.randint(0, 2)
        if match_result == 0:
            print("Match nul")
            player1[1] += 0.5
            player2[1] += 0.5
            print("Score du joueur1: ", player1[1])
            print("Score du joueur2: ", player2[1])
        elif match_result == 1:
            print(f"Victoire de {player1[0]}")
            player1[1] += 1
            print("Score du joueur1: ", player1[1])
        else:
            print(f"Victoire de {player2[0]}")
            player2[1] += 1
            print("Score du joueur2: ", player2[1])

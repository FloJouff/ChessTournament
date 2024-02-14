from views.tournament_view import TournamentView, MatchView
from models.tournament import Tournament, Round
from models.player import Player
import random
import copy
import json
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
                round_nb = input("veuillez préciser le numéro du tour: ")
                round = Round(round_nb)
                round.creation_round()
                if round_nb == "1":
                    print("Liste des matchs du 1er tour:")
                    list_of_match = RoundController.round1_generating_matches()
                else:
                    print("Liste des matchs du tour:")
                    list_of_match = RoundController.score_based_generating_matches()
                round = RoundController()
                round.run_round()
            elif choix == "4":
                print(list_of_match)
                for match in list_of_match:
                    print("-------------------------------------------")
                    player1 = match[0]
                    player2 = match[1]
                    MatchView.afficher_match(match[0], match[1])
                    MatchController.match_progress(player1, player2)
            elif choix == "5":
                Round.round_closure()
            elif choix == "6":
                data["description"] = input(
                    "Veuillez rentrer une description pour ce tournoi: "
                )
                print(data["description"])
            elif choix == "0":
                print("Quitter")
                break

    def generate_list_of_player(self, tournoi):
        players = Player.load_all_players()
        self.playerviews.afficher_list_players(players)
        while (len(tournoi.players) < 6):
            choix = input("Saissez le numéro du joueur à inclure dans le tournoi: ")
            id_player = players[int(choix)].name
            tournoi.players.append(id_player)
        return players


class RoundController:

    # Création d'une liste aléatoire, sans répétition, de tous les joueurs inscrits
    # pour le premier tour uniquement

    def round1_generating_matches():
        player_list2 = copy.deepcopy(player_list)
        random.shuffle(player_list2)

        if len(player_list2) % 2 != 0:
            print(f"le Joueur {player_list2[-1]} ne réalisera pas de match ce tour-ci, car il y a un nombre impaire de participants, il est automatiquement qualifié pour le tour suivant")
            list_of_match = [
                (player_list2[i], player_list2[i + 1])
                for i in range(0, len(player_list2)-1, 2)
            ]
            for paire in list_of_match:
                player_list2.remove(paire[0])
                player_list2.remove(paire[1])

            return list_of_match
        else:
            list_of_match = [
                (player_list2[i], player_list2[i + 1])
                for i in range(0, len(player_list2), 2)
            ]
            for paire in list_of_match:
                player_list2.remove(paire[0])
                player_list2.remove(paire[1])

            return list_of_match

    # Création d'une liste de matchs,
    # en fonction du score à l'issue des tours précédents:

    def score_based_generating_matches():
        based_score_list = sorted(Tournament.generate_list_of_player(),
                                  key=lambda x: x[1], reverse=True)   

        # je dois utiliser la liste contenant les scores à l'issu du tour précédent

        print("Liste des joueurs par ordre décroissant de score: ",
              based_score_list)
        for nom, score in based_score_list:
            print(nom, score)

        if len(based_score_list) % 2 != 0:
            print(f"le Joueur {based_score_list[0]} ne pourra pas réaliser de match, car il y a un nombre impaire de participants, il est automatiquement qualifié pour le tour suivant")         

            list_of_match = [
                (based_score_list[i], based_score_list[i + 1])
                for i in range(1, len(based_score_list), 2)
            ]
            for paire in list_of_match:
                based_score_list.remove(paire[0])
                based_score_list.remove(paire[1])

            return list_of_match
        else:
            list_of_match = [
                (based_score_list[i], based_score_list[i + 1])
                for i in range(0, len(based_score_list), 2)
            ]
            for paire in list_of_match:
                based_score_list.remove(paire[0])
                based_score_list.remove(paire[1])

            return list_of_match


class MatchController:
    def __init__(self) -> None:
        self.matchview = MatchView()

    def match_progress(player1, player2):
        match_result = random.randint(0, 2)
        if match_result == 0:
            print("Match nul")
            player1[1] += 0.5
            player2[1] += 0.5
            print(f"Score de {player1[0]}: ", player1[1])
            print(f"Score de {player2[0]}: ", player2[1])
        elif match_result == 1:
            print(f"Victoire de {player1[0]}")
            player1[1] += 1.0
            print(f"Score de {player1[0]}: ", player1[1])
        else:
            print(f"Victoire de {player2[0]}")
            player2[1] += 1.0
            print(f"Score de {player2[0]}: ", player2[1])

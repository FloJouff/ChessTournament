import random
import copy
from views.round_viewer import RoundViewer
from models.tournament import Tournament


class RoundController:
    def __init__(self) -> None:
        self.roundviewer = RoundViewer()

    def run_round(self):
        choix = ""
        while (choix != "0"):
            choix = self.roundviewer.round_menu()
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

        match = [(player_list2[i], player_list2[i + 1]) for i in range(0, len(player_list2), 2)]
        for paire in match:
            player_list2.remove(paire[0])
            player_list2.remove(paire[1])

        print(match)

    def score_based_generating_matches(self):
        scores_list.sort()
        print(scores_list)
        # il faut relier les listes de joueurs et les listes de scores
        # pour que cela soit pertinent.
        # A COMPLETER / CORRIGER
        if len(player_list) % 2 != 0:
            raise ValueError

        print("Liste des matchs du tour:")

        match = [(player_list[i], player_list[i + 1])

                 for i in range(0, len(player_list), 2)]
        for paire in match:
            player_list.remove(paire[0])
            player_list.remove(paire[1])

        print(match)

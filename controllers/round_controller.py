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

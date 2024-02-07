from datetime import datetime
from player import player_list, scores_list
import random
import copy


# un tour = une liste de match

class Round:
    def __init__(self, round_number):
        self.round_number = round_number
        self.match_list = []

# incription de l'heure du début du tour.

    def creation_round(self):
        print("Début d'un nouveau tour")
        start_time_date = datetime.now()
        print(f"Heure de début du tour {self.round_number}: ", start_time_date)

# incription de l'heure du fin du tour.

    def round_closure(self):
        print("Fin du tour")
        round_end_time = datetime.now()
        print(f"le tour {self.round_number} s'est terminé à :", round_end_time)

# Création d'une liste aléatoire, sans répétition, de tous les joueurs inscrits

    def round1_generating_matches(self):
        print("Souhaitez-vous intier le premier tour d'un tournoi?")

# cette question doit sortir de la fonction. la fonction sera appelée
# en fonction de la réponse.
        response = input("Oui (O) / Non (N): ")
        if response == "O":
            random.shuffle(player_list)
            player_list2 = copy.deepcopy(player_list)

            if len(player_list) % 2 != 0:
                raise ValueError

            print("Liste des matchs du 1er tour:")

            match = [(player_list2[i], player_list2[i + 1])
                     for i in range(0, len(player_list2), 2)]
            for paire in match:
                player_list2.remove(paire[0])
                player_list2.remove(paire[1])

            print(match)
        else:
            pass

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


round1 = Round(1)
round1.creation_round()
round1.round1_generating_matches()
# play_matchs()

round2 = Round(2)
round2.creation_round()
round2.score_based_generating_matches()

""" tenir compte du fait qu'il y a en moyenne 4 tours par tournoi!!!!"""


# round 1 = Round([matchs(round1)])
# round 2 = Round([matchs(round2)])...

from views.match_view import MatchView
from models.match import Match
import random


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

from models.player import Player


class Match:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

# fonction permettant la résolution aléatoire d'un match:

    def __repr__(self):
        return f"({self.player1[0]} vs {self.player2[0]})"


player1_name = input("Nom du joueur: ")
player1_score = float(input("Score actuel du joueur 1: "))
player2_name = input("Nom du joueur: ")
player2_score = float(input("Score actuel du joueur 2: "))
player1 = [player1_name, player1_score]
player2 = [player2_name, player2_score]
match = Match(player1, player2)

print(match)

Match.match_progress(player1, player2)

# for n in range(0, len(player_list)):
#     print(player_list[n], scores_list[n])


# match = ([joueur1, score_joueur1], [joueur2, score_joueur2])

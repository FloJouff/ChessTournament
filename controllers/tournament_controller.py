from models import player, tournament, round
import random

""" Gère les actions liées aux tournois: Création,
gestion des rounds, génération des paires, mise à jour des scores"""


def tournament_creation():
    pass


def pair_generate(player_score: list):
    player_score.sort()
    pair = ()
    for player in player_score:
        pair = (player_score[player], player_score[player + 1])
        if player_score ==:
            random.player
    pass


def score_management():
    pass


def round_management():
    pass

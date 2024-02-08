from datetime import datetime


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

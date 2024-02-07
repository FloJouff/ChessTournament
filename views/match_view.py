from models.match import Match


class MatchView:
    def afficher_match(self):
        print(Match.player1, " vs ", Match.player2)

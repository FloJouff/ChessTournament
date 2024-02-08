from models.tournament import Tournament, Match
from models.player import Player



class TournamentView:
    def __init__(self) -> None:
        self.tournament = Tournament()

    def afficher_tournoi(self):
        print(Tournament.name, Tournament.place)

    def get_tournament_infos(self):
        print("Rentrer les infos du tournois ")
        name = input("Nom du tournoi:")
        place = input("Lieu: ")
        start_date = input("Date de début: ")
        end_date = input("Date de fin: ")
        number_of_round = input("Nombre de tour pour ce tournoi: ")
        return {name, place, start_date, end_date, number_of_round}

    def register_player(self):
        print("Inscrire un participant?")
        Player.name = input("Nom du joueur: ")
        Tournament.players = []
        Tournament.players.append(Player.name)
        Player.score = 0.0
        new_list = [(nom, Player.score) for nom in Tournament.players]
        for tuple in new_list:
            print(tuple)
        print(new_list)
        return new_list

    def menu_tournoi(self):
        print("Menu tournoi")
        print("1. Pour enregistrer les informations d'un tournoi")
        print("2. Pour inscrire un participant à ce tournoi")
        print("3. Pour afficher le resultat d'un tournoi")
        print("4. Pour saisir une description ")
        print("0. Quitter")
        return input("Votre choix: ")


class RoundView:
    def round_menu(self):
        print("Menu du tour")
        print("1. Pour générer les matchs du premier tour")
        print("2. Pour générer les matchs des tours suivants")
        print("0. Quitter")
        return input("Votre choix: ")


class MatchView:
    def afficher_match(self):
        print(Match.player1, " vs ", Match.player2)

    def afficher_match_scores():
        print(Match.player1_score "  ", Match.player2_score)

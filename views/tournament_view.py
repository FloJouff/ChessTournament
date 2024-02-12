from models.tournament import Tournament
from models.player import Player


Tournament.new_list = [["Maximoff Wanda", 0.0], ["Charles Xavier", 1.0],
                       ["Eric Lensher", 0.0], ["Steve Rogers", 1.0],
                       ["Stark Tony", 0.0], ["Peter Parker", 0.5],
                       ["Howeltt James", 0.5], ["Carol Danvers", 1.0]]


class TournamentView:
    def __init__(self) -> None:
        self.tournament = Tournament("Chess Tour-nament", "Tour", "12/10/2022",
                                     "14/10/2022")

    def afficher_tournoi(self):
        print(Tournament.name, Tournament.place)

    def get_tournament_infos(self):
        print("Rentrer les informations du tournoi ")
        name = input("Nom du tournoi:")
        place = input("Lieu: ")
        start_date = input("Date de début: ")
        end_date = input("Date de fin: ")
        number_of_round = input("Nombre de tour pour ce tournoi: ")
        return {"name": name, "place": place,
                "start_date": start_date, "end_date": end_date,
                "nombre_de_tour": number_of_round}

    def register_player():
        print("Inscrire un participant?")
        Player.name = input("Nom du joueur: ")
        Tournament.players.append(Player.name)
        Player.score = 0.0
        new_list = [(nom, Player.score) for nom in Tournament.players]
        for tuple in new_list:
            print(f"Informations du joueur: {tuple[0]}:", tuple)
        print(new_list)
        return new_list

    def menu_tournoi(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("---------------  MENU DES TOURNOIS  ----------------")
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("1 --> Pour enregistrer les informations d'un tournoi")
        print("2 --> Pour inscrire un participant à ce tournoi")
        print("3 --> Pour afficher la liste des participants")
        print("4 --> Pour démarrer un nouveau tour")
        print("5 --> Pour saisir une description ")
        print("0 --> Quitter")
        return input("Votre choix: ")


class RoundView:
    def round_menu(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("-----------------  MENU DES TOURS  -----------------")
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("1 --> Pour démarrer un nouveau tour et générer les matchs")
        print("2 --> Pour résoudre aléatoirement les matchs du tour")
        print("3 --> Pour cloturer un tour")
        print("0 --> Quitter")
        return input("Votre choix: ")


class MatchView:
    def afficher_match(player1, player2):
        print(player1, " vs ", player2)

    def afficher_scores_joueurs():
        print("A l'issu des matchs de ce tour, les scores sont les suivants:")
        for player in Tournament.new_list:
            player.score += player.score
            print(f"Nouveau score de {player.name}: ", player.score)

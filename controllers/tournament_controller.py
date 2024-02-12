from views.tournament_view import TournamentView, RoundView, MatchView
from models.tournament import Tournament, Round
import random
import copy


class TournamentController:
    def __init__(self) -> None:
        self.tournamentview = TournamentView()

    def run_tournament(self):
        choix = ""
        while choix != "0":
            choix = self.tournamentview.menu_tournoi()
            if choix == "1":
                data = self.tournamentview.get_tournament_infos()
                print(data)
                tournoi = Tournament(
                    data["name"],
                    data["place"],
                    data["start_date"],
                    data["end_date"],
                    data["nombre_de_tour"],
                )
                tournoi.create_tournament()
            elif choix == "2":
                TournamentView.register_player()
            elif choix == "3":
                pass
            elif choix == "4":
                round = RoundController()
                round.run_round()
            elif choix == "5":
                data["description"] = input(
                    "Veuillez rentrer une description pour ce tournoi: "
                )
            elif choix == "0":
                print("Quitter")
                break

    def round_management():
        pass


class RoundController:
    def __init__(self) -> None:
        self.roundview = RoundView()

    def run_round(self):
        choix = ""
        while choix != "0":
            choix = self.roundview.round_menu()
            if choix == "1":
                round_nb = input("veuillez préciser le numéro du tour: ")
                round = Round(round_nb)
                round.creation_round()
                if round_nb == "1":
                    list_of_match = RoundController.round1_generating_matches()
                else:
                    list_of_match = RoundController.score_based_generating_matches()
            elif choix == "2":
                print(list_of_match)
                for match in list_of_match:
                    print("--------------------------------------")
                    player1 = match[0]
                    print("le joueur 1 est : ", player1)
                    player2 = match[1]
                    print("le joueur 2 est : ", player2)
                    MatchView.afficher_match(match[0], match[1])
                    MatchController.match_progress(player1, player2)
            elif choix == "2":
                pass
            elif choix == "3":
                Round.round_closure()
            elif choix == "0":
                print("Quitter")
                break

    # Création d'une liste aléatoire, sans répétition, de tous les joueurs inscrits

    def round1_generating_matches():
        random.shuffle(TournamentView.register_player())
        player_list2 = copy.deepcopy(TournamentView.register_player())

        if len(player_list2) % 2 != 0:
            raise ValueError

        print("Liste des matchs du 1er tour:")

        list_of_match = [
            (player_list2[i], player_list2[i + 1])
            for i in range(0, len(player_list2), 2)
        ]
        for paire in list_of_match:
            player_list2.remove(paire[0])
            player_list2.remove(paire[1])

        print(list_of_match)
        return list_of_match

    # Création d'une liste de matchs,
    # en fonction du score à l'issue des tours précédents:

    def score_based_generating_matches():
        based_score_list = sorted(Tournament.new_list, key=lambda x: x[1], reverse=True)
        print("Liste des joueurs par ordre décroissant de score: ", based_score_list)
        for nom, score in based_score_list:
            print(nom, score)

        if len(based_score_list) % 2 != 0:
            raise ValueError

        print("Liste des matchs du tour:")

        list_of_match = [
            (based_score_list[i], based_score_list[i + 1])
            for i in range(0, len(based_score_list), 2)
        ]
        for paire in list_of_match:
            based_score_list.remove(paire[0])
            based_score_list.remove(paire[1])

        print(list_of_match)
        return list_of_match


class MatchController:
    def __init__(self) -> None:
        self.matchview = MatchView()

    def match_progress(player1, player2):
        match_result = random.randint(0, 2)
        if match_result == 0:
            print("Match nul")
            player1[1] += float(0.5)
            player2[1] += float(0.5)
            print(f"Score de {player1[0]}: ", player1[1])
            print(f"Score de {player2[0]}: ", player2[1])
        elif match_result == 1:
            print(f"Victoire de {player1[0]}")
            player1[1] += float(1)
            print(f"Score de {player1[0]}: ", player1[1])
        else:
            print(f"Victoire de {player2[0]}")
            player2[1] += float(1)
            print(f"Score de {player2[0]}: ", player2[1])

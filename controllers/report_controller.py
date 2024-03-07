from views.report_view import ReportView
import Constantes.constantes as constante
from models.report import Report
from models.player import Player
from operator import attrgetter


class ReportController:
    def __init__(self) -> None:
        self.reportview = ReportView()

    def run_report(self):
        choix = ""
        while (choix != "0"):
            choix = self.reportview.menu_report()
            if choix == constante.DISPLAY_TOURNAMENT_LIST:
                data = Report.display_tournaments(self)
                for i in range(len(data)):
                    datas = [data[i]["id"], data[i]["name"], data[i]["place"],
                             data[i]["start_date"], data[i]["end_date"],
                             data[i]["description"],
                             data[i]["number_of_round"], data[i]["status"]]
                    filename = "tournois"
                    fieldnames = ["id", "nom", "lieu", "start_date",
                                  "end_date", "description",
                                  "Nb_of_round", "status"]
                    Report.add_data_to_csv(filename, fieldnames, datas)
            elif choix == constante.DISPLAY_PLAYERS_LIST:
                data = Player.load_all_players(self)
                print("Liste de tous les joueurs enregistrés dans le fichier:")
                data = sorted(data, key=attrgetter('name'))
                print(data)
                print("")
                for i in range(0, len(data)):
                    datas = [data[i].id, data[i].name, data[i].first_name,
                             data[i].gender, data[i].date_of_birth,
                             data[i].ine]
                    filename = "players"
                    fieldnames = ["id", "nom", "prénom", "sexe",
                                  "date de naissance", "ine"]
                    Report.add_data_to_csv(filename, fieldnames, datas)
            elif choix == constante.DISPLAY_TOURNAMENT_NAME_DATES:
                id_tournoi = ReportView.get_input(self)
                data = Report.load_tournament_by_id(id_tournoi)
                print("")
                print("Nom du tournoi :", data.name, "Date de début: ",
                      data.start_date, "Date de fin: ", data.end_date)
                print("")
                datas = [id_tournoi, data.name, data.start_date, data.end_date]
                filename = data.name
                fieldnames = ["id", "nom", "Date de début", "Date de fin"]
                Report.add_data_to_csv(filename, fieldnames, datas)
            elif choix == constante.DISPLAY_TOURNAMENT_LIST_PLAYER:
                print("Liste des tournois: ")
                tournoi = Report.display_tournaments(self)
                print("")
                choice = input("Pour quel tournoi souhaitez vous ces informations? ")
                id_tournoi = tournoi[int(choice)]["id"]
                data = Report.get_tournament_participants_by_id(id_tournoi)
                players = []
                for player in data:
                    joueur = Player.load_player_by_id(player)
                    players.append([joueur.name, joueur.first_name, joueur.ine])
                    players.sort()
                for i in players:
                    filename = "Joueurs", tournoi[int(choice)]["name"]
                    fieldnames = ["nom", "prénom", "ine"]
                    Report.add_data_to_csv(filename, fieldnames, i)
                print("Participants :", players)
                print("")
            elif choix == constante.DISPLAY_TOURNAMENT_NUMBER_OF_ROUND:
                print("Liste des tournois: ")
                tournoi = Report.display_tournaments(self)
                print("")
                choice = input("Pour quel tournoi souhaitez vous ces informations? ")
                id_tournoi = tournoi[int(choice)]["id"]
                data = Report.get_tournament_numb_of_round_by_id(id_tournoi)
                datas = [tournoi[int(choice)]["id"],
                         tournoi[int(choice)]["name"],
                         tournoi[int(choice)]["number_of_round"]]
                filename = tournoi[int(choice)]["name"], "nb_tour"
                fieldnames = ["id", "name", "nb_tour"]
                Report.add_data_to_csv(filename, fieldnames, datas)
                print(f"Nombre de tours du tournoi de {tournoi[int(choice)]["name"]} :", data)
                print("")
            elif choix == constante.DISPLAY_TOURNAMENT_LIST_OF_MATCHS:
                print("Liste des tournois: ")
                tournoi = Report.display_tournaments(self)
                print("")
                choice = input("Pour quel tournoi souhaitez vous ces informations? ")
                id_tournoi = tournoi[int(choice)]["id"]
                filename = tournoi[int(choice)]["name"], "Matchs"
                fieldnames = ["id", "name", "round", "matchs"]
                round_list = Report.display_rounds_matchs(id_tournoi)
                for list in round_list:
                    datas = [tournoi[int(choice)]["id"], tournoi[int(choice)]["name"], list[0], list[1]]
                    Report.add_data_to_csv(filename, fieldnames, datas)
            elif choix == "0":
                print("Quitter")
                break

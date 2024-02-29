from views.report_view import ReportView
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
            if choix == "1":
                data = Report.display_tournaments()
                for i in range(len(data)):
                    datas = [data[i]["id"], data[i]["name"], data[i]["place"],
                             data[i]["start_date"], data[i]["end_date"],
                             data[i]["players"], data[i]["description"],
                             data[i]["number_of_round"], data[i]["rounds"],
                             data[i]["status"]]
                    filename = "tournois"
                    fieldnames = ["id", "nom", "lieu", "start_date",
                                  "end_date", "players", "description",
                                  "Nb_of_round", "rounds", "status"]
                    Report.add_data_to_csv(filename, fieldnames, datas)
            elif choix == "2":
                data = Player.load_all_players()
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
            elif choix == "3":
                print("Liste des tournois: ")
                tournoi = Report.display_tournaments()
                print("")
                choice = input("Pour quel tournoi souhaitez vous ces informations? ")
                id_tournoi = tournoi[int(choice)]["id"]
                data = Report.load_tournament_by_id(id_tournoi)
                print("")
                print("Nom du tournoi :", data.name, "Date de début: ",
                      data.start_date, "Date de fin: ", data.end_date)
                print("")
                datas = [data.id, data.name, data.start_date, data.end_date]
                filename = data.name
                fieldnames = ["id", "nom", "Date de début", "Date de fin"]
                Report.add_data_to_csv(filename, fieldnames, datas)
            elif choix == "4":
                print("Liste des tournois: ")
                tournoi = Report.display_tournaments()
                print("")
                choice = input("Pour quel tournoi souhaitez vous ces informations? ")
                id_tournoi = tournoi[int(choice)]["id"]
                data = Report.get_tournament_participants_by_id(id_tournoi)
                players = []
                print("data :", data)
                for player in data:
                    joueur = Player.load_player_by_id(player)
                    print("Joueur: ", joueur.name)
                    players.append(joueur.name)
                    players.sort()
                    datas = [joueur.id, joueur.name, joueur.first_name,
                             joueur.ine]
                    filename = "Joueurs", tournoi[int(choice)]["name"]
                    fieldnames = ["id", "nom", "prénom", "ine"]
                    Report.add_data_to_csv(filename, fieldnames, datas)
                print("Participants :", players)
                print("")
            elif choix == "5":
                print("Liste des tournois: ")
                tournoi = Report.display_tournaments()
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
            elif choix == "6":
                print("Liste des tournois: ")
                tournoi = Report.display_tournaments()
                print("")
                choice = input("Pour quel tournoi souhaitez vous ces informations? ")
                id_tournoi = tournoi[int(choice)]["id"]
                round = input("De quel tour voulez vous les matchs?")
                data = Report.display_matches_per_round(id_tournoi, round)
                datas = [tournoi[int(choice)]["id"],
                         tournoi[int(choice)]["name"], round, data]
                filename = tournoi[int(choice)]["name"], f"round{round}", "Matchs"
                fieldnames = ["id", "name", "round", "matchs"]
                Report.add_data_to_csv(filename, fieldnames, datas)
            elif choix == "0":
                print("Quitter")
                break

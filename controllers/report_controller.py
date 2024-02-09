from views.report_view import ReportView
""" Gère la génération des rapports demandés"""


class ReportController:
    def __init__(self) -> None:
        self.reportview = ReportView()

        def run_report(self):
            choix = ""
            while (choix != "0"):
                choix = self.reportview.menu_report()
                if choix == "1":
                    pass
                elif choix == "2":
                    pass
                elif choix == "0":
                    print("Quitter")
                    break

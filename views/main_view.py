import Constantes.constantes as constante


class MainView:
    def menu_principal(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("--BIENVENUE SUR LE GESTIONNAIRE DE TOURNOIS D'ECHECS--")
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("------------------  MENU PRINCIPAL  ------------------")
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print(f"{constante.PLAYER_MENU} --> Pour accéder au menu des joueurs")
        print(f"{constante.TOURNAMENT_MENU} --> Pour accéder au menu des tournois")
        print(f"{constante.REPORT_MENU} --> Pour accéder au menu des rapports")
        print("0 --> Pour Quitter")
        print("")
        return input("Votre choix: ")

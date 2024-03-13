from controllers.main_controller import MainController
import os
import json

if not os.path.isfile("data/player_data.json"):
    os.makedirs("data", exist_ok=True)
    with open("data/player_data.json", "w") as f:
        json.dump([], f)

if not os.path.isfile("data/tournaments.json"):
    with open("data/tournaments.json", "w") as f:
        json.dump([], f)


def main():
    main_controller = MainController()
    main_controller.run_main_controller()


if __name__ == main():
    main()

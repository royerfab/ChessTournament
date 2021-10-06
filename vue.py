class View:

    def prompt_for_player(self):
        last_name = input("tapez le nom du joueur : ")
        first_name = input("tapez le prénom du joueur : ")
        date_of_birth = input("tapez la date de naissance du joueur : ")
        sexe = input("tapez le sexe du joueur : ")
        classement = input("tapez le classement du joueur : ")
        if not last_name or first_name or date_of_birth or sexe or classement :
            return None
        if sexe != 'H' or sexe != 'F' :
            return None
        return last_name, first_name, date_of_birth, sexe, classement

    def prompt_for_tournament(self):
        name = input("tapez le nom du tournoi : ")
        place = input("tapez le lieu du tournoi : ")
        date = input("tapez la date du tournoi : ")
        rounds = input("tapez le nombre de tours : ")
        players = input("tapez le nombre de joueurs : ")
        time_control = input("tapez le temps du tournoi : ")
        description = input("tapez la description du tournoi : ")
        if not name or place or date or rounds or players or time_control or description :
            return None
        return name, place, date, rounds, players, time_control, description

    def write_result(self):
        result = input("tapez le nom du vainqueur : ")
        return result

    def prompt_for_new_game(self):
        print("Souhaitez vous refaire un match ?")
        choice = input("Y/n: ")
        if choice == "n":
            return False
        return True
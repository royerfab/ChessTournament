from modele import Player

class View:

    def menu(self):
        print("Bienvenue")
        print("\n")
        create_player = input("Créer un joueur")
        create_tournament = input("Créer un tournoi")
        show_lists = input("Voir les listes")
        update_ranking = input("Modifier le classement")
        if create_player:
            self.prompt_for_player()
        if create_tournament:
            self.prompt_for_tournament()
        if show_lists:
            self.show_lists()
        if update_ranking:
            self.update_ranking()


class player_view:

    def prompt_for_player(self):
        last_name = input("tapez le nom du joueur : ")
        first_name = input("tapez le prénom du joueur : ")
        date_of_birth = input("tapez la date de naissance du joueur : ")
        sexe = input("tapez le sexe du joueur : ")
        classement = input("tapez le classement du joueur : ")
        back = input("Retour")
        if not last_name or first_name or date_of_birth or sexe or classement :
            return None
        if sexe != 'H' or sexe != 'F' :
            return None
        if back:
            self.menu()
        return last_name, first_name, date_of_birth, sexe, classement

class tournament_view:

    def prompt_for_tournament(self):
        name = input("tapez le nom du tournoi : ")
        place = input("tapez le lieu du tournoi : ")
        date = input("tapez la date du tournoi : ")
        rounds = input("tapez le nombre de tours : ")
        players = input("tapez le nombre de joueurs : ")
        time_control = input("tapez le temps du tournoi : ")
        description = input("tapez la description du tournoi : ")
        choose_players = input("Choisissez huit joueurs")
        validate_tournament = input("Valider la création d'un tournoi")
        back = input("Retour")
        if not name or place or date or rounds or players or time_control or description or choose_players :
            return None
        if validate_tournament:
            self.create_first_turn()
        if back:
            self.menu()
        return name, place, date, rounds, players, time_control, description, choose_players

    def create_first_turn(self):
        turn_name = input("Tapez le nom du tour :")
        validate_turn = input("Générer automatiquement des paires et lancer le premier tour")
        back = input("Retour")
        if not turn_name:
            return None
        if validate_turn:
            self.create_other_turn()
        if back:
            self.prompt_for_tournament()

    def create_other_turns(self):
        result_1 = input("Tapez le résultat du joueur 1 :")
        result_2 = input("Tapez le résultat du joueur 1 :")
        turn_name = input("Tapez le nom du tour :")
        validate_turn = input("Générer automatiquement des paires et lancer un nouveau tour")
        end_tournament = input("Mettre fin au tournoi")
        if not result_1 or result_2:
            return None
        if validate_turn and not turn_name:
            return None
        if validate_turn:
            self.create_other_turn()
        if end_tournament:
            self.update_ranking()

    def update_ranking(self):
        update_ranking = input("Taper le nom du joueur et son nouveau rang :")
        back = input("Retour au menu")
        if back:
            self.menu()

class lists:

    def show_lists(self):
        alphabetic_actor_list = input("Liste des acteurs par ordre alphabétique")
        rank_actor_list = input("Liste des acteurs selon le classement")
        alphabetic_player_list = input("Liste des joueurs par ordre alphabétique")
        rank_player_list = input("Liste des acteurs par ordre alphabétique")
        tournaments_list = input("Liste des tournois")
        turns_list = input("Liste des tours d'un tournoi")
        matchs_list = input("Liste des matchs d'un tournoi")
        if alphabetic_player_list:
            print(players)
        if tournaments_list:
            print(tournaments)
        if turns_list:
            self.turns_list()
        if matchs_list:
            self.matchs_list()

    def turns_list(self):
        turns_list = input("Tapez le nom du tournoi :")
        back = input("Retour")
        if not turns_list:
            return None
        if turns_list:
            print()
        if back:
            self.show_lists()

    def matchs_list(self):
        matchs_list = input("Tapez le nom du tournoi :")
        back = input("Retour")
        if not matchs_list:
            return None
        if matchs_list:
            print()
        if back:
            self.show_lists()

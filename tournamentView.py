from modele import Tournament

class TournamentView:

    def menu(self):
        print("Bienvenue")
        print("\n")
        print("Entrez le numéro correspondant à l'action que vous souhaitez accomplir."
              "1 Créer un joueur"
              "2 Créer un tournoi"
              "3 Voir les listes de joueurs"
              "4 Voir les listes de tournois"
              "5 Modifier le classement")
        choix = input("Tapez votre choix")
        choice = int(choix)
        if choice == 1:
            self.prompt_for_player()
        elif choice == 2:
            self.prompt_for_tournament()
        elif choice == 3:
            self.show_lists_player()
        elif choice == 4:
            self.show_lists_tournament()
        elif choice == 5:
            self.update_ranking()
        elif choice != 1 or 2 or 3 or 4 or 5:
            print("Le choix n'est pas valide !!!")
            self.menu()

    def prompt_for_tournament(self):
        name = input("tapez le nom du tournoi : ")
        place = input("tapez le lieu du tournoi : ")
        date = input("tapez la date du tournoi : ")
        rounds = input("tapez le nombre de tours : ")
        players = input("tapez le nombre de joueurs : ")
        time_control = input("tapez le temps du tournoi : ")
        description = input("tapez la description du tournoi : ")
        new_tournament = {'name': name, 'place': place, 'date': date, 'rounds': rounds, 'players': players, 'time_control': time_control, 'description': description}
        choose_players = input("Choisissez huit joueurs")
        print("Entrez le numéro correspondant à l'action que vous souhaitez accomplir."
              "1 Valider la création d'un tournoi"
              "2 Revenir au menu")
        choix = input("Tapez votre choix")
        choice = int(choix)
        if choice == 1 and not name or not place or not date or not rounds or not players or not time_control or not description or not choose_players :
            print("Il manque une information!!!")
            self.prompt_for_tournament()
        elif choice == 1:
            self.create_first_turn()
            return new_tournament
            return choose_players
        elif choice == 2:
            self.menu()
        else:
            print("Le choix n'est pas valide!!!")
            self.prompt_for_tournament()

    def create_first_turn(self):
        turn_name = input("Tapez le nom du tour :")
        print("Entrez le numéro correspondant à l'action que vous souhaitez accomplir."
              "1 Valider la création d'un tour"
              "2 Revenir au menu")
        choix = input("Tapez votre choix")
        choice = int(choix)
        if choice == 1 and not turn_name:
            print("Il manque une information!!!")
            self.create_first_turn()
        elif choice == 1:
            self.create_other_turn()
            return turn_name
        elif choice == 2:
            self.prompt_for_tournament()
        else:
            print("Le choix n'est pas valide!!!")
            self.create_first_turn()


    def create_other_turns(self):
        result_1 = input("Tapez le résultat du joueur 1 :")
        result_2 = input("Tapez le résultat du joueur 1 :")
        turn_name = input("Tapez le nom du tour :")
        print("Entrez le numéro correspondant à l'action que vous souhaitez accomplir."
              "1 Valider la création d'un tour"
              "2 Mettre fin au tournoi")
        choix = input("Tapez votre choix")
        choice = int(choix)
        if choice == 1 and not turn_name or not result_1 or not result_2:
            print("Il manque une information!!!")
            self.create_other_turns()
        elif choice == 2 and not result_1 or not result_2:
            print("Il manque une information!!!")
            self.create_other_turns()
        elif choice == 1:
            self.create_other_turn()
            return turn_name, result_1, result_2
        elif choice == 2:
            self.update_ranking()
            return result_1, result_2
        else:
            print("Le choix n'est pas valide!!!")
            self.create_other_turns()

    def update_ranking_menu(self):
        update_ranking_name = input("Taper le nom du joueur :")
        update_ranking_rank = input("Taper le nouveau rang du joueur :")
        print("Entrez le numéro correspondant à l'action que vous souhaitez accomplir."
              "1 Valider la modification du classement d'un joueur"
              "2 Revenir au menu")
        choix = input("Tapez votre choix")
        choice = int(choix)
        if choice == 1 and not update_ranking_name or not update_ranking_rank:
            print("Il manque une information!!!")
            self.update_ranking_menu()
        elif choice == 1:
            self.menu()
            return update_ranking_name, update_ranking_rank
        elif choice == 2:
            self.menu()
        else:
            print("Le choix n'est pas valide!!!")
            self.update_ranking_menu()

    def show_lists_tournament(self):
        print("Entrez le numéro correspondant à l'action que vous souhaitez accomplir."
              "1 Liste des tournois"
              "2 Liste des tours d'un tournoi"
              "3 Liste des matchs d'un tournoi"
              "4 Revenir au menu")
        choix = input("Tapez votre choix")
        choice = int(choix)
        if choice == 1:
            print()
        elif choice == 2:
            self.turns_list()
        elif choice == 3:
            self.matchs_list()
        elif choice == 4:
            self.menu()
        else:
            print("Le choix n'est pas valide!!!")
            self.show_lists_tournament()

    def turns_list(self):
        turns_list = input("Tapez le nom du tournoi :")
        print("Entrez le numéro correspondant à l'action que vous souhaitez accomplir."
              "1 Valider la recherche"
              "2 Retour")
        choix = input("Tapez votre choix")
        choice = int(choix)
        if choice == 1 and not turns_list:
            print("Il manque une information!!!")
            self.turns_list()
        elif choice == 1:
            print()
        elif choice == 2:
            self.show_lists_tournament()
        else:
            print("Le choix n'est pas valide!!!")
            self.turns_list()

    def matchs_list(self):
        matchs_list = input("Tapez le nom du tournoi :")
        print("Entrez le numéro correspondant à l'action que vous souhaitez accomplir."
              "1 Valider la recherche"
              "2 Retour")
        choix = input("Tapez votre choix")
        choice = int(choix)
        if choice == 1 and not matchs_list:
            print("Une information n'est pas valide!!!")
            self.matchs_list()
        elif choice == 1:
            print()
        elif choice == 2:
            self.show_lists_tournament()
        else:
            print("Le choix n'est pas valide!!!")
            self.matchs_list()


tournamentView = TournamentView()
tournamentView.menu()
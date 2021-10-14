from modele import Player

class playerView:

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

    def prompt_for_player(self):
        last_name = input("tapez le nom du joueur : ")
        first_name = input("tapez le prénom du joueur : ")
        date_of_birth = input("tapez la date de naissance du joueur : ")
        sexe = input("tapez le sexe du joueur : ")
        classement = input("tapez le classement du joueur : ")
        new_player = {'last_name': last_name, 'first_name': first_name, 'date_of_birth': date_of_birth, 'sexe': sexe, 'classement': classement}
        print("Entrez le numéro correspondant à l'action que vous souhaitez accomplir."
              "1 Valider la création d'un joueur"
              "2 Revenir au menu")
        choix = input("Tapez votre choix")
        choice = int(choix)
        if choice == 1 and not last_name or first_name or date_of_birth or sexe or classement :
            return None
        elif sexe != 'H' or sexe != 'F' :
            return None
        elif choice == 1:
            return new_player
            self.menu()
        elif choice == 2:
            self.menu()
        else:
            print("Le choix n'est pas valide!!!")
            self.prompt_for_player()

    def show_lists_player(self):
        print("Entrez le numéro correspondant à l'action que vous souhaitez accomplir."
              "1 Liste des joueurs par ordre alphabétique"
              "2 Liste des joueurs selon le classement"
              "3 Liste des acteurs par ordre alphabétique"
              "4 Liste des acteurs selon le classement"
              "5 Revenir au menu")
        choix = input("Tapez votre choix")
        choice = int(choix)
        if choice == 1:
            print()
        elif choice == 2:
            print()
        elif choice == 3:
            print()
        elif choice == 4:
            print()
        elif choice == 5:
            self.menu()
        else:
            print("Le choix n'est pas valide!!!")
            self.show_lists_player()

playerView = playerView()
playerView.menu()
from modele import Player, Tournament
import playerView
import tournamentView
import numpy

class playerController:
    def create_player(self, new_player):
        playerView.prompt_for_player()
        if input == 1:
            player = Player(new_player)


    def create_player(self, new_player):
        playerView.prompt_for_player()
        if input == 1:
            Player.create(new_player)

    def players_alphabetic_order(self, players):
        playerView.show_lists_player()
        if input == 2:
            sorted_list = sorted(Player.getAllPlayer())
            print(sorted_list)

    def players_rank_order(self, players):
        playerView.show_lists_player()
        if input == 2:
            sorted_list = sorted(Player.getAllPlayer())
            print(sorted_list)

class tournamentController:

    def create_tournament(self, new_tournament):
        tournamentView.prompt_for_tournament()
        if input == 1:
            tournament = Tournament(new_tournament)

    def first_turn(self):
        tournamentView.create_first_turn()
        if input == 1:
            players_turn = numpy.random.choice(choose_players, 2)
            return players_turn

    players_turn = numpy.random.sample(choose_players, 8)

    def other_turn(self):
        tournamentView.create_other_turn()
        if input == 1:
            players_turn = numpy.random.choice(choose_players, 2)
            return players_turn


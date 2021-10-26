from modele import Player, Tournament
from playerView import PlayerView
from tournamentView import TournamentView
import random

class PlayerController:

    playerView = PlayerView()
    tournamentView = TournamentView()

    def create_player(self):
        try:
            new_player = self.playerView.prompt_for_player()
            player = Player(**new_player)
            player.create()
            return True
        except Exception as e:
            print('Erreur:', str(e))
            return False

    def players_alphabetic_order(self, players):
        try:
            players = Player.getAll()
            self.playerView.show_lists_player(players)
            return True
        except Exception as e:
            print('Erreur:', str(e))
            return False

class tournamentController:

    def create_tournament(self, new_tournament):
        try:
            new_tournament = self.tournamentView.prompt_for_tournament()
            tournament = Tournament(**new_tournament)
            tournament.create()
            return True
        except Exception as e:
            print('Erreur:', str(e))
            return False

    def first_turn(self):
        try:
            self.tournamentView.prompt_for_tournament()
            self.tournamentView.create_first_turn()
            players_turn = random.choice(choose_players, 8)
            return players_turn
            return True
        except Exception as e:
            print('Erreur:', str(e))
            return False

    def other_turn(self):
        try:
            self.TournamentView.create_other_turns()
            #players_turn = numpy.random.choice(choose_players, 2)
            #return players_turn
            return True
        except Exception as e:
            print('Erreur:', str(e))
            return False

    def update_ranking(self):
        try:
            update_player = self.playerView.update_ranking_menu()
            player = update_ranking_name
            player.update({'classement': str(update_ranking_rank)}, Player.type == update_ranking_name)
            return True
        except Exception as e:
            print('Erreur:', str(e))
            return False
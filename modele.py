import mvc_exceptions as mvc_exc
from tinydb import TinyDB, Query

class Player:
    id = None
    def __init__(self, last_name, first_name, date_of_birth, sexe, classement):
        self.last_name = last_name
        self.first_name = first_name
        self.date_of_birth = date_of_birth
        self.sexe = sexe
        self.classement = classement
        #indiquer que le chiffre est forcément positif? Mettre if où on réupère la valeur

class Tournaments:
    def __init__(self, name, rounds):
        name =
        rounds = 4
        round_name = 1
        for round in rounds:
            round_name += 1
            running = True
            while running:
                self.view.informations_tour()
                self.match()
                running = self.view.prompt_for_new_game()

# variable globale
players =  list()

#CRUD pour la classe players
def create_players(app_players):
         global players
         players = app_players

def create_player(last_name, first_name, date_of_birth, sexe, classement):
            global players
            results = list(filter(lambda x: x['last_name'] == last_name, players))
            if results:
                raise mvc_exc.ItemAlreadyStored('"{}" already stored!'.format(last_name))
            else:
                players.append({'last_name': last_name, 'first_name': first_name, 'date_of_birth': date_of_birth, 'sexe': sexe, 'classement': classement})



def read_player(last_name):
    global players
    myplayers = list(filter(lambda x: x['last_name'] == last_name, players))
    if myplayers:
        return myplayers[0]
    else:
        raise mvc_exc.ItemNotStored('Can\'t read "{}" because it\'s not stored'.format(last_name))


def read_players():
    global players
    return [player for player in players]


def update_player(last_name, first_name, date_of_birth, sexe, classement):
    global players
    idxs_players = list(filter(lambda i_x: i_x[1]['last_name'] == last_name, enumerate(players)))
    if idxs_players:
        i, player_to_update = idxs_players[0][0], idxs_players[0][1]
        players[i] = {'last_name': last_name, 'first_name': first_name, 'date_of_birth': date_of_birth, 'sexe': sexe, 'classement': classement}
    else:
        raise mvc_exc.ItemNotStored('Can\'t update "{}" because it\'s not stored'.format(last_name))


def delete_player(last_name):
    global players
    idxs_players = list(filter(lambda i_x: i_x[1]['last_name'] == last_name, enumerate(players)))
    if idxs_players:
        i, player_to_delete = idxs_players[0][0], idxs_players[0][1]
        del players[i]
    else:
        raise mvc_exc.ItemNotStored('Can\'t delete "{}" because it\'s not stored'.format(last_name))


 # variable globale
tournaments =  list()

#CRUD pour la classe tournament
def create_tournaments(app_tournaments):
         global tournaments
         tournaments = app_tournaments

def create_tournament(name, rounds):
            global tournaments
            results = list(filter(lambda x: x['last_name'] == name, tournaments))
            if results:
                raise mvc_exc.ItemAlreadyStored('"{}" already stored!'.format(name))
            else:
                tournaments.append({'name': name, 'rounds': rounds})



def read_tournaments(name):
    global players
    mytournaments = list(filter(lambda x: x['name'] == name, tournaments))
    if mytournaments:
        return mytournaments[0]
    else:
        raise mvc_exc.ItemNotStored('Can\'t read "{}" because it\'s not stored'.format(name))


def read_tournaments():
    global tournaments
    return [tournament for tournament in tournaments]


def update_tournament(name, rounds):
    global tournaments
    idxs_tournaments = list(filter(lambda i_x: i_x[1]['name'] == name, enumerate(tournaments)))
    if idxs_tournaments:
        i, tournament_to_update = idxs_tournaments[0][0], idxs_tournaments[0][1]
        tournaments[i] = {'name': name, 'rounds': rounds}
    else:
        raise mvc_exc.ItemNotStored('Can\'t update "{}" because it\'s not stored'.format(name))


def delete_tournament(name):
    global tournaments
    idxs_tournaments = list(filter(lambda i_x: i_x[1]['name'] == name, enumerate(tournaments)))
    if idxs_tournaments:
        i, tournament_to_delete = idxs_tournaments[0][0], idxs_tournaments[0][1]
        del tournaments[i]
    else:
        raise mvc_exc.ItemNotStored('Can\'t delete "{}" because it\'s not stored'.format(name))

#tinydb
db = TinyDB('db.json')
db.insert(players)
db.insert(tournaments)
db.all()
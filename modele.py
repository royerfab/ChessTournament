from tinydb import TinyDB, Query

db = TinyDB('db.json')

class Player:
    id = None
    def __init__(self, last_name, first_name, date_of_birth, sexe, classement):
        self.last_name = last_name
        self.first_name = first_name
        self.date_of_birth = date_of_birth
        self.sexe = sexe
        self.classement = classement
        #indiquer que le chiffre est forcément positif? Mettre if où on réupère la valeur

    def serialize(self):
        player = {'last_name': self.last_name, 'first_name': self.first_name, 'date_of_birth': self.date_of_birth, 'sexe': self.sexe, 'classement': self.classement}
        return player

    @classmethod
    def deserialize(cls, player):
        last_name = player['last_name']
        first_name = player['first_name']
        date_of_birth = player['date_of_birth']
        sexe = player['sexe']
        classement = player['classement']
        player = Player(last_name=last_name, first_name=first_name, date_of_birth=date_of_birth, sexe=sexe, classement=classement)
        return player

    def create(self):
        db.insert(self.serialize())

    @classmethod
    def read(cls, last_name):
        playerQuery = Query()
        results = db.search(playerQuery.last_name == last_name)
        player = Player.deserialize(results[0])
        for result in results:
            print(result)

    def update(self, last_name):
        playerQuery = Query()
        results = db.search(playerQuery.last_name == last_name)
        player = Player.deserialize(results[0])
        db.update(playerQuery.last_name == last_name)

    def delete(self, last_name):
        playerQuery = Query()
        results = db.search(playerQuery.last_name == last_name)
        player = Player.deserialize(results[0])
        db.remove(self.deserialize)

class Tournament:
    def __init__(self, name, place, date, rounds, players, time_control, description):
        self.name = name
        self.place = place
        self.date = date
        self.rounds = rounds
        self. players = players
        self.time_control = time_control
        self.description = description


    def serialize(self):
        tournament = {'name': self.name, 'place': self.place, 'date': self.date, 'rounds': self.rounds, 'players': self.players, 'time_control': self.time_control, 'descirption': self.description}
        return tournament

    def deserialize(self, tournament):
        name = tournament['name']
        place = tournament['place']
        date = tournament['date']
        rounds = tournament['rounds']
        players = tournament['players']
        time_control = tournament['time_control']
        description = tournament['description']
        tournament = Tournament(name=name, place=place, date=date, rounds=rounds, players=players, time_control=time_control, description=description)
        return tournament

    def create(self):
        db.insert(self.serialize())

    @classmethod
    def read(cls, name):
        tournamentQuery = Query()
        results = db.search(tournamentQuery.name == name)
        tournament = Tournament.deserialize(results[0])
        for result in results:
            print(result)

    def update(self, name):
        tournamentQuery = Query()
        results = db.search(tournamentQuery.name == name)
        tournament = Tournament.deserialize(results[0])
        db.update(tournamentQuery.name == name)

    def delete(self, name):
        tournamentQuery = Query()
        results = db.search(tournamentQuery.name == name)
        tournament = Tournament.deserialize(results[0])
        db.remove(self)

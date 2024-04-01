class Player:

    def __init__(self, name, team):
        self.name = name
        self.xp = 1500
        self.team = team

    def introduce(self):
        print(f"Hello! I'm {self.name} and I play for {self.team}")

class Team:

    def __init__(self, team_name):
        self.name = team_name
        self.players = []
        self.xp = 0

    def show_players(self):
        for player in self.players:
            player.introduce()

    def add_player(self, name):
        new_player = Player(name, self.name)
        self.players.append(new_player)
        self.xp = self.xp + new_player.xp

    def remove_player(self, name):
        for player in self.players:
            if name == player.name:
                self.players.remove(player)
                self.xp = self.xp - player.xp

    def total_xp(self):
        print(f"This team sum amount xp {self.xp}")


team_X = Team("Team X")
team_X.add_player("discphy")

blue_team = Team("Team Blue")
team_X.add_player("Lynn")

team_X.total_xp()

team_X.remove_player("discphy")
team_X.remove_player("Lynn")

team_X.total_xp()

def create_player_for_team(name, xp, team):
    pass

def create_player(name, xp, team):
    return {
        "name": name,
        "XP": xp,
        "team": team
    }


def introduce_player(player):
    name = player["name"]
    team = player["team"]
    print(f"Hello! My name is {name} and I play for {team}")


discphy = create_player("Discphy", 1000, "Team X")
lynn = create_player("Lynn", 1500, "Team Blue")

teams = {
    "Team X": [discphy],
    "Team Blue": [lynn]
}

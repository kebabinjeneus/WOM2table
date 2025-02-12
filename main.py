import player
import json

numberOfTeams = int(input("Give the number of teams: "))
teamPlayers = []
for x in range(numberOfTeams):
	players = input("Give the usernames of the players of team " + str(x) + " in a csv format (name1,name2,name3): ")
	teamPlayers.append(players)

participants = []
for i in range(numberOfTeams):
	participants.append(player.getTeam(teamPlayers[i-1]))

for t in participants:
	player.getOverview(t)

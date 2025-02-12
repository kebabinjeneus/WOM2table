import player
import json

numberOfTeams = int(input("Give the number of teams: "))
teamPlayers = []
for x in range(numberOfTeams):
	players = input("Give the rsn and commitment of the players of team " + str(x) + " in the following format (name1.hours1,n2.h2,n3.h3): ")
	teamPlayers.append(players)

participants = []
for i in range(numberOfTeams):
	participants.append(player.getTeam(teamPlayers[i-1]))

for t in participants:
	player.getOverview(t)

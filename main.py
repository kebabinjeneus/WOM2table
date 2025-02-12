import player
import json

numberOfTeams = 1
given  = input("Give the number of teams: ")
if given != '':
	numberOfTeams = int(given)

# get all players per team for all teams and skip if no players are given
teamPlayers = []
for x in range(numberOfTeams):
	players = input("Give the rsn and commitment of the players of team " + str(x) + " in the following format (name1.hours1,n2.h2,n3.h3): ")
	if players != '':
		teamPlayers.append(players)
	else:
		numberOfTeams -= 1

# parse the team players given in the previous step and get data from WOM API
participants = []
for i in range(numberOfTeams):
	participants.append(player.getTeam(teamPlayers[i]))

# print a table of team players per team
for t in participants:
	player.getOverview(t)


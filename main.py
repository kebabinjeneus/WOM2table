import player
import json
import time

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

totalParticipants = 0
for teams in teamPlayers:
	totalParticipants += len(teams)

# parse the team players given in the previous step and get data from WOM API
participants = []
if totalParticipants <= 20:
	for i in range(numberOfTeams):
		participants.append(player.getTeam(teamPlayers[i]))
	# print a table of team players per team
	for t in participants:
		player.getOverview(t)
else:
	for i in range(numberOfTeams):
		participants.append(player.getTeam(teamPlayers[i]))
		player.getOverview(participants[i])
		if i < numberOfTeams-1:
			print("Waiting for 60 seconds due to API limits. . .")
			for i in range(60,0,-1):
				time.sleep(1)
				print('\033[1A\033[12C'+'{:02d}'.format(i))

import requests
import json
import time
from prettytable import PrettyTable

#APIiterations = 1

def getPlayer(ign):
	player = json.loads(requests.get("https://api.wiseoldman.net/v2/players/" + ign).text)
	return player


def getTeam(players):
	team  = []
	igns = players.split(',')
	for x in igns:
		team.append(getPlayer(x))
		#if APIiterations%20 == 0:
		#	print('waiting for API rate-limit, program paused for 60s')
		#	time.sleep(60)
		#APIiterations += 1
	return team

def getOverview(team):
	overview = PrettyTable(['RSN', 'CB', 'Tot.', 'Type'])
	for p in team:
		overview.add_row(getStats(p))
	overview.reversesort = True
	print(overview.get_string(sortby='Tot.'))
	overview.clear_rows()

def getStats(player):
	stats = [
		player.get('username'), 
		player.get('combatLevel'),
		player.get("latestSnapshot").get("data").get("skills").get("overall").get('level'),
		player.get('type')
		]
	return stats

	


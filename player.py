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
	igns = players.split(",")
	for x in igns:
		team.append(getPlayer(x))
		#if APIiterations%20 == 0:
		#	print("waiting for API rate-limit, program paused for 60s")
		#	time.sleep(60)
		#APIiterations += 1
	return team

def getOverview(team):
	overview = PrettyTable(["RSN", "CB", "Tot.", "Type", "Raids", "RaidsCM"])
	for p in team:
		overview.add_row(getStats(p))
	overview.reversesort = True
	print(overview.get_string(sortby="Tot."))
	overview.clear_rows()

def getStats(player):
	skills = player["latestSnapshot"]["data"]["skills"]
	bosses = player["latestSnapshot"]["data"]["bosses"]
	raids = bosses["chambers_of_xeric"]["kills"] + bosses["tombs_of_amascut"]["kills"] + bosses["theatre_of_blood"]["kills"]
	raidsCM = bosses["chambers_of_xeric_challenge_mode"]["kills"] + bosses["tombs_of_amascut_expert"]["kills"] + bosses["theatre_of_blood_hard_mode"]["kills"]
	stats = [
		player["username"], 
		player["combatLevel"],
		skills["overall"]["level"],
		player["type"],
		raids, 
		raidsCM
		]
	return stats

	


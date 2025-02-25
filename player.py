import requests
import json
import time
from prettytable import PrettyTable

# loads player data using the WOM API
def getPlayer(ign):
	player = json.loads(requests.get("https://api.wiseoldman.net/v2/players/" + ign).text)
	return player

# parse rsn's and commitment (if applicable) from team string and put player data in team list to return
def getTeam(players):
	team  = []
	igns = players.split(",")
	for x in igns:
		dat = x.split(".")
		dat[0] = getPlayer(dat[0])
		team.append(dat)
	return team

# compile the overview from the data in the program
def getOverview(team):
	head = ["RSN", "country", "Commitment", "CB", "Tot.", "Type", "Raids", "RaidsCM"]
	rows = []
	for p in team:
		rows.append(getStats(p))
	empty = getEmptyColumns(rows)
	if len(empty) > 0:
		for e in range(len(empty),0,-1):
			head.pop(empty[e-1])
			for row in rows:
				row.pop(empty[e-1])

	# fill the table for printing
	overview = PrettyTable()
	overview.reversesort = True
	overview.field_names = head
	overview.add_rows(rows)

	print(overview.get_string(sortby="Tot."))
	overview.clear_rows() # if this is not here it'll not create a new table for the next team

# does what's on the tin
def getEmptyColumns(rows):
	empty = []
	for col in range(len(rows[0])):
		if checkColumnClear(rows,col):
			empty.append(col)
	return empty

# iterates a column through all rows to check if empty
def checkColumnClear(rows,col):
	for row in rows:
		if row[col] != '':
			return False
	return True

def checkRaid(player, name, boss):
    bosses = player[0]["latestSnapshot"]["data"]["bosses"]
    kc = bosses[boss]["kills"]
    if kc < 1:
        return ""
    else:
        return name + ": " + str(kc)
	
# parse the playerdata to get the stats for the final overview in a neat list
def getStats(player):
	if len(player) == 2:
		commitment = player[1]
	else:
		commitment = ""
	# add a bit of readability to the stats list by pre-defining some points in the dictionary
	skills = player[0]["latestSnapshot"]["data"]["skills"]
	bosses = player[0]["latestSnapshot"]["data"]["bosses"]
	raids = checkRaid(player,"cox", "chambers_of_xeric") + checkRaid(player,"\ntoa","tombs_of_amascut") + checkRaid(player,"\ntob","theatre_of_blood")
	raidsCM = checkRaid(player,"cox", "chambers_of_xeric_challenge_mode") + checkRaid(player,"\ntoa","tombs_of_amascut_expert") + checkRaid(player,"\ntob","theatre_of_blood_hard_mode")
	#raids = "cox: " + str(bosses["chambers_of_xeric"]["kills"]) + "\ntoa: " + str(bosses["tombs_of_amascut"]["kills"]) + "\ntob: " + str(bosses["theatre_of_blood"]["kills"])
	#raidsCM = "cox: " + str(bosses["chambers_of_xeric_challenge_mode"]["kills"]) + "\ntoa: " + str(bosses["tombs_of_amascut_expert"]["kills"]) + "\ntob: " + str(bosses["theatre_of_blood_hard_mode"]["kills"])

	# remove empty results from the table
	#if raids < 1:
	#	raids = ''
	#if raidsCM < 1:
	#	raidsCM = ''
	
	stats = [
		player[0]["username"], 
        player[0]["country"],
		commitment,
		player[0]["combatLevel"],
		skills["overall"]["level"],
		player[0]["type"],
		raids, 
		raidsCM
		]
	return stats

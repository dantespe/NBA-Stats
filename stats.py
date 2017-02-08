import requests
import datetime
import json
import csv

#########################
###      CONFIG      ###
#######################
BASE_PARAMS = {
    'DateFrom': "", #type: str; format month/day/year
    "DateTo": "", #str format month/day/year
    "GameScope": "",
    "GameSegment": "",
    "LastNGames": 82,
    "LeagueID": "00",
    "Location": "",
    "MeasureType": "Advanced",
    "Month": 0,
    "OpponentTeamID": "0",
    "Outcome": "",
    "PaceAdjust": "N",
    "PerMode": "Totals",
    "Period": "0",
    "PlayerExperience": "",
    "PlayerPosition": "",
    "PlusMinus": "N",
    "Rank": "N",
    #"Season": "%s", #format 2015-16
    "SeasonSegment": "",
    "SeasonType": "Regular Season",
    "StarterBench": "",
    "VsConference": "",
    "VsDivision": ""
}

BASE_URL = "http://stats.nba.com/stats/leaguedashplayerstats"

def get_query_year(year):
    now = datetime.datetime.now()
    first_year = now.year - 1
    second_year = (now.year) % 1000

    #Stats are not available before 1946
    if year >= 1946 and year <= now.year - 1:
        first_year = str(year)
        second_year = (year + 1) % 1000

    if second_year < 10:
        #syntax should be 00 not 0
        second_year = '0' + str(second_year)
    return str(first_year) + "-" + str(second_year)

def get_data_for_season(year):
    year = get_query_year(year)
    query = BASE_PARAMS
    query['Season'] = year

    data = requests.get(BASE_URL, params=query)
    return data.json()

print get_data_for_season(2009)

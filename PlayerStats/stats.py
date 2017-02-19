import requests
import datetime
import json
import sys, os, csv
#########################
###      CONFIG      ###
#######################
### First available season would be 1997-98
MAX_RETRIES = -1

DEFAULT_TIMEOUT = 5

BASE_PARAMS = {
    #Check the README for all acceptable
    'DateFrom': "", #type: str; format month/day/year
    "DateTo": "", #str format month/day/year
    "GameScope": "", #Yesterday or Last 10
    "GameSegment": "",
    "LastNGames": 82,
    "LeagueID": "00", #00 for nba 20 for d-league
    "Location": "", #home or road
    "MeasureType": "Base", #(Base)|(Advanced)|(Misc)|(Four Factors)|(Scoring)|(Opponent)|(Usage)|(Defense)
    "Month": 0,
    "OpponentTeamID": "0",
    "Outcome": "",
    "PaceAdjust": "N", #Y or N
    "PerMode": "Totals",
    "Period": "0",
    "PlayerExperience": "",
    "PlayerPosition": "", #((F)|(C)|(G)|(C-F)|(F-C)|(F-G)|(G-F))
    "PlusMinus": "N", #Y or N
    "Rank": "Y", #Y or No
    #"Season": "%s", #format 2015-16
    "SeasonSegment": "",
    "SeasonType": "Regular Season", #(Regular Season)|(Pre Season)|(Playoffs)|(All Star)
    "StarterBench": "", #Starters or Bench
    "VsConference": "", #East or West
    "VsDivision": "" #((Atlantic)|(Central)|(Northwest)|(Pacific)|(Southeast)|(Southwest)|(East)|(West))
}

BASE_URL = "http://stats.nba.com/stats/leaguedashplayerstats"

def get_query_year(year, current=False):
    now = datetime.datetime.now()

    #Stats are not available before 1997
    if year < 1997 or year > now.year:
        current = True #ignoring the year

    if current:
        if now.month <= 6: #NBA season ends in June
            year = now.year - 1
            first_year = now.year - 1
            second_year = (now.year) % 100
        else:
            year = now.year
            first_year = now.year
            second_year = (now.year + 1) % 100
    else:
        first_year = year
        second_year = (year + 1) % 100

    if second_year < 10:
        #syntax should be 00 not 0
        second_year = '0' + str(second_year)
    return str(first_year) + "-" + str(second_year)

def get_data_for_season(year=0, current=False, retries=0):
    q_year = get_query_year(year, current=current)
    query = BASE_PARAMS
    query['Season'] = q_year

    try:
        data = requests.get(BASE_URL, params=query, timeout=DEFAULT_TIMEOUT)
        data = data.json()['resultSets'][0]
    except ValueError:
        if retries >  MAX_RETRIES:
            print 'Query url: %s' % data.url
            print 'Failed to pull data from nba.com for %s' % year
            print "Try again later."
            sys.exit(1)
        retries += 1
        return get_data_for_season(year, retries=retries)
    except requests.exceptions.ReadTimeout as e:
        if retries > MAX_RETRIES:
            print 'Failed to pull data from nba.com due to Timeout Error'
            sys.exit(1)
        retries += 1
        return get_data_for_season(year, retries=retries)

    return data

def write_stats_for_season(year, filename=None, folder=None, append=False):
    q_year = get_query_year(year)
    fname = filename if filename else '%s-Player-Stats.csv' % q_year
    full_path = fname if not folder else os.path.join(folder, fname)

    data = get_data_for_season(year)
    headers = data['headers']
    player_data = data['rowSet']

    file_perm = 'ab' if append else 'wb'

    with open(full_path, file_perm) as file_ouput:
        csv_writer = csv.writer(file_ouput)
        csv_writer.writerow(headers)
        csv_writer.writerows(player_data)

write_stats_for_season(1997, folder='data/')

import requests

url = "http://stats.nba.com/stats/leaguedashplayerstats?DateFrom=&DateTo=&GameScope=&GameSegment=&LastNGames=15&LeagueID=00&Location=&MeasureType=Advanced&Month=0&OpponentTeamID=0&Outcome=&PaceAdjust=N&PerMode=Totals&Period=0&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season=2015-16&SeasonSegment=&SeasonType=Regular+Season&StarterBench=&VsConference=&VsDivision="

data = requests.get(url)
entries = data.json()

for i in entries:
    print i

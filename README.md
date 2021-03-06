# NBA Stats REST API
[Git Repo](https://github.com/dantespe/NBA-Stats)

This project is designed to be a python wrapper  the [nba.com](stats.nba.com)'s Stats REST API. Currently this only has a wrapper to write (.csv) and return (json) data from the leaguedashplayerstats endpoint. I will continue to support the repo by adding functionality for more endpoints.


## Usage
### leaguedashplayerstats (PlayerStats.stats)
This endpoint offers the functionality of receiving player stats for players dating back to the 1997-98 season. I have yet to find basic measurements such as PPG, RBP, and APG, however, it looks like nba.com is just calculating all of those on the fly from total <unit> divided by games played.

#### Configuring Queries for leaguedashplayerstats
The leaguedashplayerstats endpoint has 25 required parameters. All of the parameters can be found in PlayerStats/stats.py as BASE_PARAMS.

The first is `DateFrom` which is in the format:  `mm/dd/yyyy`.

The next is `DateTo` which is in the format:
`mm/dd/yyyy`.

The range from `DateFrom` to `DateTo` represents the timeframe of statistics.

NOTE: `DateFrom` to `DateTo` should be within the range of `Season`.

`GameScope` can be either `Yesterday` or `Last 10`. This is a quick shorthand way to get stats from yesterday or the last 10 games.

`GameSegment` can be either `First Half`, `Second Half`, or `Overtime`. If you want to specify the part of the game.

`LastNGames` is an integer that returns stats for the last N games.

`LeagueID` can be either `00` for the NBA or `20` for the NBA Developmental League.

`Location` can be either `home` or `road`.

`MeasureType` can be any of `Base`, `Advanced`, `Misc`, `Four Factors`, `Scoring`, `Opponent`, `Usage`, or `Defense`.


`Month` can be `0` to `12`.

`OpponentTeamID` is clearly the team of ID of the opponent. You can find them [here](https://github.com/seemethere/nba_py/wiki/stats.nba.com-Endpoint-Documentation) under the Team IDs section.

`Outcome` can be `W` or `L`.

`PaceAdjust` can be either `Y` or `N`.

`Season` is in the form `YYYY-YY`. For example, `2016-17` would be the current season.

`SeasonType` can be `Regular`, `Pre Season`, `Playoffs`, or `All Star`.

`StarterBench` can be `Starters` or `Bench`.

`VsConference` can be `East` or `West`.

`VsDivision` can be `Atlantic`, `Central`, `Pacific`
, `Northwest`, `Southeast`, `Southwest`, `East`, or `West`.

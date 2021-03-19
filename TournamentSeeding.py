from sportsreference.ncaab.boxscore import Boxscores
import datetime
import numpy as np

dates_firstRound = [datetime.date(2019, 3, 21), datetime.date(2019, 3, 22),
                    datetime.date(2018, 3, 15), datetime.date(2018, 3, 16),
                    datetime.date(2017, 3, 16), datetime.date(2017, 3, 17),
                    datetime.date(2016, 3, 17), datetime.date(2016, 3, 18),
                    datetime.date(2015, 3, 19), datetime.date(2015, 3, 20),
                    datetime.date(2014, 3, 20), datetime.date(2014, 3, 21),
                    datetime.date(2013, 3, 21), datetime.date(2013, 3, 22),
                    datetime.date(2012, 3, 15), datetime.date(2012, 3, 16),
                    datetime.date(2011, 3, 17), datetime.date(2011, 3, 18),
                    datetime.date(2010, 3, 18), datetime.date(2010, 3, 19),
                    datetime.date(2009, 3, 19), datetime.date(2009, 3, 20)]
sSum = np.zeros(16)
sCount = np.zeros(16)
for dDate in dates_firstRound:
    gameList = Boxscores(dDate).games
    for day in gameList:
        for game in gameList[day]:
            hRank = game['home_rank']
            vRank = game['away_rank']
            hTeam = game['home_name']
            vTeam = game['away_name']
            hScore = game['home_score']
            vScore = game['away_score']
            hDiff = hScore - vScore
            vDiff = -hDiff
            if not(hRank is None or vRank is None):
                sSum[hRank - 1] += hDiff
                sCount[hRank - 1] += 1
                sSum[vRank - 1] += vDiff
                sCount[vRank - 1] += 1

                print("[#{:d} {:s} {:d} - #{:d} {:s} {:d}]".format(hRank, hTeam, hScore, vRank, vTeam, vScore))

for i in range(0,16):
    rank = i + 1
    print("{:d}: {:.1f}".format(rank, sSum[i]/sCount[i]))

from datetime import date
import pickle

from sportsreference.ncaab.boxscore import Boxscores
from sportsreference.ncaab.teams import Teams


def main():
    min_date = date(2021, 11, 9)
    max_date = date(2022, 3, 12)

    print("Fetching Games")
    boxs = Boxscores(min_date, max_date)

    print("Writing Games")
    with open('gamelist_20220312.pkl', 'wb') as fh:
        pickle.dump(boxs.games, fh)

    print("Fetching Teams")
    teams = Teams()

    print("Writing Teams")
    with open('teamlist_20220312.pkl', 'wb') as fh:
        pickle.dump(teams, fh)


if __name__ == '__main__':
    main()

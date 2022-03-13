from datetime import date
import pickle

from sportsreference.ncaab.boxscore import Boxscores
from sportsreference.ncaab.teams import Teams


def main():
    min_date = date(2021, 11, 9)
    max_date = date(2022, 1, 22)

    print("Fetching Games")
    boxs = Boxscores(min_date, max_date)

    print("Writing Games")
    with open('gamelist_20220123.pkl', 'wb') as fh:
        pickle.dump(boxs.games, fh)

    print("Fetching Teams")
    teams = Teams()

    print("Writing Teams")
    with open('teamlist_20220123.pkl', 'wb') as fh:
        pickle.dump(teams.games, fh)


if __name__ == '__main__':
    main()

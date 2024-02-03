from datetime import date
import pickle

from sportsipy.ncaab.boxscore import Boxscores
from sportsipy.ncaab.teams import Teams


def main():
    min_date = date(2023, 11, 5)
    max_date = date(2024, 1, 26)

    print("Fetching Games")
    boxs = Boxscores(min_date, max_date)

    print("Writing Games")
    with open('../../data/gamelist_20240127.pkl', 'wb') as fh:
        pickle.dump(boxs.games, fh)

    print("Fetching Teams")
    teams = Teams()

    print("Writing Teams")
    with open('../../data/teamlist_20240127.pkl', 'wb') as fh:
        pickle.dump(teams, fh)

if __name__ == '__main__':
    main()

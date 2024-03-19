# Reads season of games and saves so only have to scrape once
from datetime import date
import pickle

import cbbpy.mens_scraper as scraper


def main():
    c_season = 2024

    print("Fetching Games")
    tups = scraper.get_games_season(c_season, box=False, pbp=False)

    print("Writing Games")
    with open('../../data/gamelist_20240319.pkl', 'wb') as fh:
        pickle.dump(tups, fh)

    # print("Fetching Teams")
    # teams = Teams()
    #
    # print("Writing Teams")
    # with open('../../data/teamlist_20240127.pkl', 'wb') as fh:
    #     pickle.dump(teams, fh)


if __name__ == '__main__':
    main()

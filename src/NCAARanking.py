# Ranks basketball teams using genetic algorithms
import pickle
import numpy as np
import pandas as pd


def main():
    with open('data/gamelist_20220123.pkl', 'rb') as fh:
        game_list = pickle.load(fh)

    with open("data/teamlist_20220123.pkl", 'rb') as fh:
        teams = pickle.load(fh)



if __name__ == '__main__':
    main()

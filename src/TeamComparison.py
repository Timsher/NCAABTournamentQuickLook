# GUI for comparing 2 basketball teams
# Author Jon Starr <timsher@gmail.com>
# Date created: 03/12/2022
# Date last modified: 03/12/2022
import pickle
import tkinter as tk
from tkinter import ttk

import numpy as np

from sportsreference.ncaab.boxscore import Boxscore
import sportsreference.ncaab.teams


def get_games(team_name, game_list, team_list):
    opponent_rank = []
    matchup = []
    team_score = []
    opponent_score = []
    location = []

    for day in game_list:
        for game in day:
            if game.home_name == team_name:
                opponent_rank.append(team_list[game.away_abbr].simple_rating_system)
                matchup.append(game.away_name)
                team_score.append(game.home_score)
                opponent_score.append(game.away_score)
                location.append('vs')
            elif game.away_name == team_name:
                opponent_rank.append(team_list[game.home_abbr].simple_rating_system)
                matchup.append(game.home_name)
                team_score.append(game.away_score)
                opponent_score.append(game.home_score)
                location.append('home')
    opponent_rank = np.array(opponent_rank)
    opponent_score = np.array(opponent_score)
    matchup = np.array(matchup)
    team_score = np.array(team_score)
    location = np.array(location)
    index = np.argsort(opponent_rank)
    opponent_rank = opponent_rank[index]
    opponent_score = opponent_score[index]
    matchup = matchup[index]
    team_score = team_score[index]
    location = location[index]
    ret_strings = []
    for i in range(0, opponent_rank.size):
        ret_strings.append("{:.1f} {:s} {:s} {:d}-{:d}".format(opponent_rank[i], location[i], matchup[i],
                                                               team_score[i], opponent_score[i]))


def main():
    GAMEFILE = '../data/gamelist_20220312.pkl'
    TEAMFILE = '../data/teamlist_20220312.pkl'

    with open(GAMEFILE, 'rb') as fh:
        game_list = pickle.load(fh)

    with open(TEAMFILE, 'rb') as fh:
        team_list = pickle.load(fh)

    team_name_list = []
    for t in team_list:
        team_name_list.append(t.name)

    win = tk.Tk()
    win.title("NCAA Basketball Team Comparison")
    label_left = ttk.Label(win, text="Team A")
    label_left.grid(column=0, row=0)
    label_right = ttk.Label(win, text="Team B")
    label_right.grid(column=1, row=0)

    team_name_left = tk.StringVar()
    tbox_left = ttk.Combobox(win, width=40, textvariable=team_name_left)
    tbox_left['values'] = team_name_list
    tbox_left.grid(column=0, row=1)
    tbox_left.current(0)

    team_name_right = tk.StringVar()
    tbox_right = ttk.Combobox(win, width=40, textvariable=team_name_right)
    tbox_right['values'] = team_name_list
    tbox_right.grid(column=1, row=1)
    tbox_right.current(1)

    win.mainloop()


if __name__ == "__main__":
    main()

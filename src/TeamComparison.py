# GUI for comparing 2 basketball teams
# Author Jon Starr <timsher@gmail.com>
# Date created: 03/12/2022
# Date last modified: 03/12/2022
import pickle
import tkinter as tk
from tkinter import ttk
import datetime

import numpy as np
import pandas as pd


def get_games(team_name, game_list):
    """
    Given an abbreviation of a team returns a list of games played by that team and whether they won or lost
    :param team_name: Name of team to get game list from
    :param game_list: panda dataframe of all games played during current season
    :return: List of games played by that team, list of whether they won or lost
    """
    opponent_rank = []
    matchup = []
    team_score = []
    opponent_score = []
    location = []
    date_list = []

    # d_date = date(int(day_str[2]), int(day_str[0]), int(day_str[1]))
    cleaned_list = game_list.query("home_team == \"{:s}\" or away_team == \"{:s}\"".format(team_name, team_name))
    for idx, game in cleaned_list.iterrows():
        d_date = datetime.datetime.strptime(game['game_day'], "%B %d, %Y")
        if game['home_team'].lower() == team_name.lower():
            try:
                opponent_rank.append(game['away_bracket'])
            except ValueError:
                opponent_rank.append(-99.9)
            date_list.append('({:02d}/{:02d})'.format(d_date.month, d_date.day))
            matchup.append(game['away_team'])
            team_score.append(game['home_score'])
            opponent_score.append(game['away_score'])
            location.append('vs')
        elif game['away_team'].lower() == team_name.lower():
            try:
                opponent_rank.append(game['home_bracket'])
            except ValueError:
                opponent_rank.append(-99.9)
            date_list.append('({:02d}/{:02d})'.format(d_date.month, d_date.day))
            matchup.append(game['home_team'])
            team_score.append(game['away_score'])
            opponent_score.append(game['home_score'])
            location.append('at')
    opponent_rank = np.array(opponent_rank)
    opponent_score = np.array(opponent_score)
    matchup = np.array(matchup)
    team_score = np.array(team_score)
    location = np.array(location)
    date_list = np.array(date_list)
    index = np.argsort(-opponent_rank)
    opponent_rank = opponent_rank[index]
    opponent_score = opponent_score[index]
    matchup = matchup[index]
    team_score = team_score[index]
    location = location[index]
    date_list = date_list[index]
    ret_strings = []
    tags = []
    for i in range(0, opponent_rank.size):
        try:
            ret_strings.append("{:s} {:.1f} {:s} {:s} {:d}-{:d}\n".format(date_list[i], opponent_rank[i], location[i],
                                                                          matchup[i], team_score[i],
                                                                          opponent_score[i]))
            if(team_score[i] > opponent_score[i]):
                tags.append('win')
            else:
                tags.append('loss')
        except TypeError:
            pass
    return ret_strings, tags


def main():
    GAMEFILE = '../data/gamelist_20240319.pkl'
    RANKINGSFILE = '../data/Rankings_20240319.csv'
    source_column = 'RPI'

    with open(GAMEFILE, 'rb') as fh:
        game_list = pickle.load(fh)[0]
    team_list = np.sort(game_list['home_team'].unique()).tolist()

    rankings = pd.read_csv(RANKINGSFILE, sep=',', header=0)
    game_list = pd.merge(game_list, rankings, left_on='home_team', right_on='Team_Name', how='left')
    game_list = game_list.rename(columns={source_column: 'home_bracket'})
    game_list = pd.merge(game_list, rankings, left_on='away_team', right_on='Team_Name', how='left')
    game_list = game_list.rename(columns={source_column: 'away_bracket'})

    def update_left_textbox(*args):
        txt_message_left, tags = get_games(team_name_left.get(), game_list)
        txtbox_left.configure(state='normal')
        txtbox_left.delete(1.0, 'end')
        for i in range(0, len(txt_message_left)):
            txtbox_left.insert('end', txt_message_left[i], tags[i])
        txtbox_left.configure(state='disabled')

    def update_right_textbox(*args):
        txt_message_right, tags = get_games(team_name_right.get(), game_list)
        txtbox_right.configure(state='normal')
        txtbox_right.delete(1.0, 'end')
        for i in range(0, len(txt_message_right)):
            txtbox_right.insert('end', txt_message_right[i], tags[i])
        txtbox_right.configure(state='disabled')

    win = tk.Tk()
    win.title("NCAA Basketball Team Comparison")
    label_left = ttk.Label(win, text="Team A")
    label_left.grid(column=0, row=0)
    label_right = ttk.Label(win, text="Team B")
    label_right.grid(column=1, row=0)

    team_name_left = tk.StringVar()
    cbox_left = ttk.Combobox(win, width=40, textvariable=team_name_left)
    cbox_left['values'] = team_list
    cbox_left.grid(column=0, row=1)
    cbox_left.current(0)

    team_name_right = tk.StringVar()
    cbox_right = ttk.Combobox(win, width=40, textvariable=team_name_right)
    cbox_right['values'] = team_list
    cbox_right.grid(column=1, row=1)
    cbox_right.current(1)

    txtbox_left = tk.Text(win, height=40, width=50)
    txtbox_left.grid(column=0, row=2)
    txtbox_left.tag_configure('win', background='#80CBC4')
    txtbox_left.tag_configure('loss', background='#EF9A9A')
    txtbox_left.configure(state='disabled')

    txtbox_right = tk.Text(win, height=40, width=50)
    txtbox_right.grid(column=1, row=2)
    txtbox_right.tag_configure('win', background='#80CBC4')
    txtbox_right.tag_configure('loss', background='#EF9A9A')
    txtbox_right.configure(state='disabled')

    team_name_right.trace('w', update_right_textbox)
    team_name_left.trace('w', update_left_textbox)

    update_right_textbox()
    update_left_textbox()

    win.mainloop()


if __name__ == "__main__":
    main()

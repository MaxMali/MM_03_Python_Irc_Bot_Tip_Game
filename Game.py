#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""
Project Bitcoin Course Tip Game

This project was created as a subtask of the Data Science module of the Media Informatics Master course.

Written by Max M., 2020
"""


class Game:

    def __init__(self, name, time_submission=10, time_round=60, max_number_of_player=5):
        self.name = name
        self.time_submission = time_submission
        self.time_round = time_round
        self.max_number_of_player = max_number_of_player

        print("Game created.")

    def reg_player(self):
        # Player registration for a round
        pass

    def create_round(self):
        # Creates a Game Round
        pass

    def save_player_tip(self):
        # Safes a tip of a player
        pass

    def end_tip_time(self):
        # End of Tip Time
        pass

    def start_tip_time(self):
        # Starts the Tip time
        pass

    def get_result(self):
        # Evaluates the result of a round
        pass

    def post_result(self):
        # Posts the result of a round
        pass

    def safe_result(self):
        # Safes the result of a round
        pass

    

#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""
Project Bitcoin Course Tip Game

This project was created as a subtask of the Data Science module of the Media Informatics Master course.

Written by Max Malinowski, 2020
Matrikel-Nr.: 70383508
Nebenhörer
"""
import requests
from Helper import get_btc_price


class Game:

    def __init__(self, name, submission_time=10, round_time=60, max_number_of_player=5):
        self.name = name
        self.time_submission = submission_time
        self.time_round = round_time
        self.max_number_of_player = max_number_of_player
        self.number_of_player = 0
        self.players = {}

        print("Game created with submission time:" + str(submission_time) + " round time:" + str(
            round_time) + " max players:" + str(max_number_of_player))

    def get_player_tip(self, name, tip):
        # Player registration for a round

        if self.number_of_player < self.max_number_of_player:
            self.number_of_player += 1
            self.players.update({name: tip})
        else:
            print("Round already full. Try it next round.")

    def create_round(self):
        self.number_of_player = 0
        self.players = {}
        # Creates a Game Round
        pass

    def end_tip_time(self):
        # End of Tip Time
        print("Tip Time ends now!!!")
        pass

    def start_tip_time(self):
        # Starts the Tip time
        print("Tip Time starts now, you have 15 seconds for give a hint !!!")
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

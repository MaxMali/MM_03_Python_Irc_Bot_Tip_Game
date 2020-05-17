#!/usr/bin/python
# -*- encoding: utf-8 -*-
__author__ = 'm.malinowski'
"""
Project Bitcoin Course Tip Game

This project was created as a subtask of the Data Science module of the Media Informatics Master course.

Written by Max Malinowski, 2020
Matrikel-Nr.: 70383508
Nebenhörer
"""

import time
from Helper import get_btc_price

class Game:

    def __init__(self, name="Placeholder", submission_time=10, round_time=60, max_number_of_player=5):
        self.name = name
        self.time_submission = submission_time
        self.time_round = round_time
        self.max_number_of_player = max_number_of_player
        self.number_of_player = 0
        self.players = {}
        self.running_tip_time = False
        self.running_waiting_time = True

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
        return "Round create."

    def end_tip_time(self):
        # End of Tip Time
        print("Tip Time ends now!!!")
        pass

    def start_tip_time(self, tip_time):
        self.running_tip_time = True
        print("Tip Time starts now, you have " + tip_time + " seconds for give a hint !!!")
        while tip_time and self.running_tip_time:
            minutes, seconds = divmod(tip_time, 60)
            timer = "{:02d}:{:02d}".format(minutes, seconds)
            print(timer, end="\r")
            tip_time.sleep(1)
            tip_time -= 1
        self.running_tip_time = False
        print("Tip time over!!!")
        # Starts the Tip time

        return "Tip Time is over. Round is closed. Lets wait"

    def start_waiting_time(self, waiting_time):
        self.running_waiting_time = True
        while waiting_time and self.running_waiting_time:
            minutes, seconds = divmod(waiting_time, 60)
            timer = "{:02d}:{:02d}".format(minutes, seconds)
            print(timer, end="\r")
            waiting_time.sleep(1)
            waiting_time -= 1
        self.running_waiting_time = False
        print("Round is over. Give me one moment for the results!!!")

        return "Round is over. Give me one moment for the results"

    def get_result(self):
        # Evaluates the result of a round
        price = get_btc_price
        if len(self.players) > 0:
            print("hurz")
        else:
            print("No Players in this round")

        pass

    def post_result(self):
        # Posts the result of a round
        pass

    def safe_result(self):
        # Safes the result of a round
        pass

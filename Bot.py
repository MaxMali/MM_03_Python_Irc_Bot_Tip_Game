#!/usr/bin/python
# -*- encoding: utf-8 -*-
__author__ = 'm.malinowski'
"""
Project Bitcoin Course Tip Game

This project was created as a subtask of the Data Science module of the Media Informatics Master course.

Written by Max M., 2020

chat.freenode.net 6697  #keller1337 GameBot_Biibo
"""

import socket
import time
import sys
from Game import *
from Helper import *

CHANNEL = "#keller1337"
PASSWORD = "12344321"


class Bot:

    def __init__(self):
        self.irc_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.game = Game()  # todo hier muss die Zeile noch weg
        self.admins = ["Fals3lighT"]
        print('Socket created')

    def connect(self, server_ip, server_port, bot_nick, bot_nick_pass):
        # Connect to the IRC server
        print("Connecting to Server: ", server_ip, ":", server_port)
        self.irc_socket.connect((server_ip, server_port))

        # Perform user authentication
        self.irc_socket.send(
            bytes("USER " + bot_nick + " " + bot_nick + " " + bot_nick + " :This is a fun bot!n" + "\n", "UTF-8"))
        self.irc_socket.send(bytes("NICK " + bot_nick + "\n", "UTF-8"))
        self.irc_socket.send(bytes("NICKSERV IDENTIFY " + bot_nick + " " + bot_nick_pass + "\n", "UTF-8"))
        time.sleep(5)
        print("Connected.")

    def join_channel(self, channel):
        # Join a channel
        self.irc_socket.send(bytes("JOIN " + channel + "\n", "UTF-8"))
        print("Channel:" + channel + " joined.")
        welcoming = "Heyho, i am the GameBot Biibo. write .infos for details"
        self.send_private_msg(channel, welcoming)

    def send_text(self, text):
        # Post a text in a channel
        self.irc_socket.send(bytes(text + "\n", "UTF-8"))

    def send_private_msg(self, channel, msg):
        # Transfer data
        self.irc_socket.send(bytes("PRIVMSG " + channel + " :" + str(msg) + "\n", "UTF-8"))

    def get_text(self):
        # Get the text
        time.sleep(1)
        text = self.irc_socket.recv(2040).decode("UTF-8")

        if text.find('PING') != -1:
            self.irc_socket.send(bytes('PONG ' + text.split()[1] + '\r\n', "UTF-8"))

        return text

    def post_game_information(self, channel):
        # Bot .info - Post the game infos
        text = "This is a BTC Tip Game ! (write .help for commands and .rule for the rules)"
        self.send_private_msg(channel, text)

    def post_game_help_or_rules(self, channel, what):
        # Bot .help .rule - Post the Bot Commands or the game rules
        if what == 0:
            text = open("txts/help.txt", "r")
        else:
            text = open("txts/rules.txt", "r")
        for lines in text:
            self.send_private_msg(channel, lines)
        text.close()

    def post_btc_price(self, channel):
        # Post a countdown
        price = get_btc_price()
        text = "USD/BTC:" + str(price)
        self.send_private_msg(channel, text)

    def post_countdown(self, channel, timer):
        # Post a countdown
        text = "Timer:" + timer
        self.send_private_msg(channel, text)
        time.sleep(5)
        text = "TimerEnd:" + timer
        self.send_private_msg(channel, text)

    def start_countdown(self, channel, timer="1:20:20"):
        # Pos a countdown
        countdown_time=timer.split(":")
        hours_to_seconds = int(countdown_time[0]) * 3600
        minutes_to_seconds = int(countdown_time[1]) * 60
        cd = int(countdown_time[2]) + hours_to_seconds + minutes_to_seconds
        while cd > 0:
            print(cd)
            self.send_private_msg(channel, cd)
            cd -= 1
            time.sleep(1)
        text = "Timer:" + str(timer)
        self.send_private_msg(channel, text)


    def create_game(self, channel):
        # Create a new Game
        self.game = Game("Tip Game", 15, 30, 10)
        text = self.game.create_round()
        text_two = "Game created"
        self.send_private_msg(channel, text)
        self.send_private_msg(channel, text_two)
        return True

    '''
    Admin functions
    '''

    def check_admin_user(self, user_name):
        # Checks if a User has admin rights
        if user_name in self.admins:
            return True
        else:
            return False

    def get_admin_rights(self, channel, user_name, bot_password):
        # Checks the password and give user rights
        if PASSWORD in bot_password:
            self.admins.append(user_name)
            self.send_private_msg(channel, "You got admins rights, " + user_name + "!")
        else:
            self.send_private_msg(channel, "Bad password!!!")

    def show_admins(self, channel):
        # Checks if a User has admin rights
        self.send_private_msg(channel, "Admins:")
        for admin in self.admins:
            self.send_private_msg(channel, admin)
        return True

    '''
    Bot command "interpreter" functions
    '''

    def command(self, command, user_name):
        # Interpreting the irc commands

        if "hello" in command:
            self.send_private_msg(CHANNEL, "Hello!")
            return True

        elif ".info" in command:
            self.post_game_information(CHANNEL)
            return True

        elif ".btcprice" in command:
            self.post_btc_price(CHANNEL)
            return True

        elif ".startc" in command:
            self.start_countdown(CHANNEL, "1:10:10")
            return True

        elif ".help" in command:
            self.post_game_help_or_rules(CHANNEL, 0)
            return True

        elif ".rule" in command:
            self.post_game_help_or_rules(CHANNEL, 1)
            return True

        elif ".startgame" in command:
            if self.create_game(CHANNEL):
                self.send_private_msg(CHANNEL, "Game created!")
            else:
                self.send_private_msg(CHANNEL, "Game not created!")
            self.send_private_msg(CHANNEL, "Hello!")
            return True

        elif ".start c" in command:
            self.post_countdown(CHANNEL, "30")
            return True

        elif ".showadmins" in command:
            self.show_admins(CHANNEL)
            return True

            # Admin commands
        elif ".go away!!" in command:
            if self.check_admin_user(user_name) is True:
                self.close_connection()
                return False
            else:
                self.send_private_msg(CHANNEL, "No rights...dont try this " + user_name)
                return True

        elif ".givemepower" in command:
            bot_password = command.rsplit(" ")
            self.get_admin_rights(CHANNEL, user_name, bot_password[1])
            return True

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
from Helper import get_btc_price

HELP_TEXT = "the bot commands will be explained here"
GAME_RULES = "the game rules will be explained here"


class Bot:

    def __init__(self):
        self.irc_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.game = Game()  # todo hier muss die Zeile noch weg
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
        self.irc_socket.send(bytes("PRIVMSG " + channel + " :" + msg + "\n", "UTF-8"))

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
            self.send_private_msg(channel, HELP_TEXT)
        else:
            self.send_private_msg(channel, GAME_RULES)



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

    def create_game(self, channel):
        self.game = Game("Tip Game", 15, 30, 10)
        text = self.game.create_round()
        text_two = "Game created"
        self.send_private_msg(channel, text)
        self.send_private_msg(channel, text_two)

        return True

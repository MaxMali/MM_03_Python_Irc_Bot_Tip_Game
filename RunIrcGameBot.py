#!/usr/bin/python
# -*- encoding: utf-8 -*-
__author__ = 'm.malinowski'
"""
Project Bitcoin Course Tip Game

This project was created as a subtask of the Data Science module of the Media Informatics Master course.

Written by Max M., 2020
"""

from Bot import *
import os
import random

# IRC Config


loop = True
server_ip = "chat.freenode.net"  # Provide a valid server IP/Hostname
server_port = 6667
channel = "#keller1337"
bot_nick = "GameBot_Biibo"
bot_nick_pass = "xxx"
irc = Bot()
irc.connect(server_ip, server_port, bot_nick, bot_nick_pass)
irc.join_channel(channel)

while loop:
    text = irc.get_text()
    print(text)

    if "PRIVMSG" in text and channel in text and "hello" in text:
        irc.send_private_msg(channel, "Hello!")

    if "PRIVMSG" in text and channel in text and "go away!!" in text:
        irc.close_connection()
        loop = False

    if "PRIVMSG" in text and channel in text and "start c" in text:
        irc.post_countdown(channel, "30")

    if "PRIVMSG" in text and channel in text and ".info" in text:
        irc.post_game_information(channel)

    if "PRIVMSG" in text and channel in text and ".btcprice" in text:
        irc.post_btc_price(channel)
    if "PRIVMSG" in text and channel in text and ".help" in text:
        irc.post_game_help_or_rules(channel, 0)
    if "PRIVMSG" in text and channel in text and ".rule" in text:
        irc.post_game_help_or_rules(channel, 1)

    if "PRIVMSG" in text and channel in text and ".startgame" in text:
        if irc.create_game(channel):
            irc.send_private_msg(channel, "Game created!")
        else:
            irc.send_private_msg(channel, "Game not created!")

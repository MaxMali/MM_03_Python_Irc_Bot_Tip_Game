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

    if "PRIVMSG" in text and channel in text:

        command = text.rsplit(":")
        loop = irc.command(command[2])









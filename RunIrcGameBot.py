#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""
Project Bitcoin Course Tip Game

This project was created as a subtask of the Data Science module of the Media Informatics Master course.

Written by Max M., 2020
"""

from Bot import *
import os
import random

# IRC Config

run = True
server_ip = "chat.freenode.net"  # Provide a valid server IP/Hostname
server_port = 6667
channel = "#keller1337"
bot_nick = "GameBot_Biibo"
bot_nick_pass = "xxx"
irc = Bot()
irc.connect(server_ip, server_port, bot_nick, bot_nick_pass)
irc.join_channel(channel)

while run:
    text = irc.get_text()
    print(text)

    if "PRIVMSG" in text and channel in text and "hello" in text:
        irc.send_private_msg(channel, "Hello!")

    if "PRIVMSG" in text and channel in text and "geh weg!" in text:
        irc.close_connection()
        run = False

    if "PRIVMSG" in text and channel in text and "start c" in text:
        irc.post_countdown(channel, "30")
#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""
Project Bitcoin Course Tip Game

This project was created as a subtask of the Data Science module of the Media Informatics Master course.

Written by Max M., 2020

chat.freenode.net 6697  #keller1337 GameBot_Biibo
"""

import socket
import time
import sys


class Bot:

    def __init__(self):
        self.irc_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
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

    def send_text(self, text):
        # Post a text in a channel
        self.irc_socket.send(bytes(text + "\n", "UTF-8"))

    def send_private_msg(self, channel, msg):
        # Transfer data
        self.irc_socket.send(bytes("PRIVMSG " + channel + " " + msg + "\n", "UTF-8"))

    def post_countdown(self, channel, timer):
        # Post a countdown
        self.irc_socket.send(bytes("PRIVMSG " + channel + " Timer:" + timer + "\n", "UTF-8"))
        time.sleep(5)
        self.irc_socket.send(bytes("PRIVMSG " + channel + " Timer:END" + timer + "\n", "UTF-8"))

    def get_text(self):
        # Get the text
        time.sleep(1)
        text = self.irc_socket.recv(2040).decode("UTF-8")

        if text.find('PING') != -1:
            self.irc_socket.send(bytes('PONG ' + text.split()[1] + '\r\n', "UTF-8"))

        return text

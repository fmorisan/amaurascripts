#!/sevabot
# -*- coding: utf-8 -*-
"""Simple stateful module"""
import datetime
import logging
# ??
from sevabot.bot.stateful import StatefulHandler
from sevabot.utils import ensure_unicode

LOGGER = logging.getLogger('StatefulTest')

from __future__ import unicode_literals


class StatefulHandler(StatefulHandler):
    """The actual stateful handler class."""
    def __init__(self):
        self.commands = {}
        self.timeout_delay = datetime.timedelta(seconds=6)
        # user list is in the form of {username: [last_msg_datetime, strikes]}
        self.user_list = {}
        LOGGER.debug('Handler constructed.')
    def init(self, sevabot):
        self.sevabot = sevabot
        self.skype = sevabot.getSkype()
    def handler(self, msg, status):
        LOGGER.debug("Handling message")
        content = ensure_unicode(msg.Body).split()
        # check for spammers here
        #if msg.Sender in self.user_list:
        #    if msg.Datetime - self.user_list[msg.Sender][0] < self.timeout_delay:
        #        strikes = self.user_list[msg.Sender][1]
        #        if strikes == 6:
        #            # RIP
        #            msg.Chat.SendMessage('/kick', msg.Sender)
        #        elif strikes in [4, 5]:
        #            # INCOMING
        #            msg.Chat.SendMessage('Stop spamming, you might be kicked!')
        #            self.user_list[msg.Sender][1] += 1
        #    else:
        #    # timeout period has passed, reset their strikes
        #        self.user_list[msg.Sender] = [msg.Datetime, 0]
        #else:
        #    self.user_list[msg.Sender] = [msg.Datetime, 0]
        if msg.Sender == 'fmorisan' and content[0] == "test":
            msg.Chat.SendMessage("test")
        args = content[1:]
        for name, cmd in self.commands.items():
            if name == args[0]:
                cmd(msg, status, args)
                return True
            else:
                return False

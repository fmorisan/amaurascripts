#!/sevabot

# -*- coding: utf-8 -*-

"""
Simple conference call hosting
"""
from __future__ import unicode_literals

import logging
import Skype4Py

from sevabot.bot.stateful import StatefulSkypeHandler
from sevabot.utils import ensure_unicode
import time
import json

logger = logging.getLogger('Stateful')

# Set to debug only during dev
logger.setLevel(logging.INFO)

logger.debug('Call module level load import')


class Handler(StatefulSkypeHandler):

    """
    Skype message handler class for the conference call hosting.
    """

    def __init__(self):
        """
        Use `init` method to initialize a handler.
        """

        logger.debug('Call handler constructed')

    def init(self, sevabot):
        """
        Set-up our state. This is called every time module is (re)loaded.
        :param skype: Handle to Skype4Py instance
        """

        logger.debug('Call handler init')

        self.skype = sevabot.getSkype()
        self.calls = {}
        self.userlist = {}
        self.timeoutTime = 5
        self.sp = True
        self.oplist = ["fmorisan", "euphoricradioactivity"]
        try:
            self.banlist = json.load(open(sharedVars.bannedFile, "r"))
        except:
            # file not there?
            self.banlist = []

        self.commands = {}

    def handle_message(self, msg, status):
        """
        Override this method to customize a handler.
        """

        body = ensure_unicode(msg.Body)

        logger.debug('Call handler got: {}'.format(body))

        # If the separators are not specified, runs of consecutive
        # whitespace are regarded as a single separator
        words = body.split()
        handle = msg.Sender.Handle

        if not len(words) or handle == 'alchemisbot':
            return True

        if handle not in self.userlist:
            self.userlist[handle] = [int(time.time()), 0]

        if time.time() - self.userlist[handle][0] < self.timeoutTime and self.sp:
            self.userlist[handle][1] += 1
        else:
            self.userlist[handle][1] = 0

        if self.userlist[handle][1] in [4,5]:
            msg.Chat.SendMessage("Stop flooding, {}! You might get kicked from the chat! Wait {}s before posting again.".format(handle, int(self.timeoutTime-time.time()+self.userlist[handle][0])))
        if self.userlist[handle][1] >= 6:
            msg.Chat.SendMessage("/kick {}".format(handle))

        if handle in self.oplist:
            if body == "sp":
                self.sp = not self.sp
                msg.Chat.SendMessage("sp is now " + ["off","on"][self.sp]) # False is 0, True is 1
                # hax because bool is a subclass of int and thus can be used as a list index
            if body.startswith("!ban"):
                self.banlist.append(words[1])
                msg.Chat.SendMessage("User {} banned from bot interaction.".format(words[1]))
            if body.startswith("!unban"):
                self.banlist.remove(words[1])
                msg.Chat.SendMessage("User {} unbanned from bot interaction.".format(words[1]))
        
        if handle in self.banlist:
            return True
        
        if handle not in self.oplist and body == "!reload":
            return True
            # ignore reloads done by people who are not chat operators
        
        self.userlist[handle][0] = time.time()
        return False

    def shutdown():
        """
        Called when the module is reloaded.
        """
        json.dump(self.banlist, open(sharedVars.bannedFile, "w"))
        logger.debug('Call handler shutdown')

    def help(self, msg, status, args):
        """
        Show help message to the sender.
        """
        msg.Chat.SendMessage(HELP_TEXT)

# Export the instance to Sevabot
sevabot_handler = Handler()

__all__ = ['sevabot_handler']
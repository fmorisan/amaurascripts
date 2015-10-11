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

logger = logging.getLogger('Call')

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

        self.commands = {'help': self.help, 'start': self.start_call, 'end': self.end_call}

    def handle_message(self, msg, status):
        """
        Override this method to customize a handler.
        """

        body = ensure_unicode(msg.Body)

        logger.debug('Call handler got: {}'.format(body))

        # If the separators are not specified, runs of consecutive
        # whitespace are regarded as a single separator
        words = body.split()

        if not len(words):
            return False

        if body == "test" and msg.Sender.Handle == "fmorisan":
                msg.Chat.SendMessage("test")
                return True
        return False

    def shutdown():
        """
        Called when the module is reloaded.
        """
        logger.debug('Call handler shutdown')

    def help(self, msg, status, args):
        """
        Show help message to the sender.
        """
        msg.Chat.SendMessage(HELP_TEXT)

    def is_call_active(self, chat_name=None):
        """
        Is a call from the chat active?
        """
        pass

    def start_call(self, msg, status, args):
        """
        Start a conference call of the chat if any call is not active.
        """
	pass

    def end_call(self, msg, status, args):
        """
        Finish a conference call of the chat.
        """
        pass

# Export the instance to Sevabot
sevabot_handler = Handler()

__all__ = ['sevabot_handler']
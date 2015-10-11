#!/sevabot
 
# -*- coding: utf-8 -*-
 
"""
Simple conference call hosting
"""
from __future__ import unicode_literals
import traceback
import logging
import Skype4Py
import os
import sys
import subprocess
import json
 
# Markov generator stuff.
import random
import redis
 
# time based commands
from time import sleep
 
from sevabot.bot.stateful import StatefulSkypeHandler
from sevabot.utils import ensure_unicode
 
 
 
logger = logging.getLogger('TestStateful')
 
# Set to debug only during dev
logger.setLevel(logging.DEBUG)
 
logger.debug('test module level load import')
 
HELP_TEXT = """Simple conference call hosting allows you to have bot host a conference call from the chat.
 
Sevabot can have only one conference call at the same instance.
 
Commands:
 
!call help: Show this help text
 
!call: Start a conference call from the chat
 
!call start: Same as !call
 
!call end: Finish the conference call from the chat
"""
 
class CallHandler(StatefulSkypeHandler):
 
        """
        Skype message handler class for the conference call hosting.
        """
 
        def __init__(self):
                """
                Use `init` method to initialize a handler.
                """
                logger.debug('test handler constructed')
                self.spState = False
        def init(self, sevabot):
                """
                Set-up our state. This is called every time module is (re)loaded.
 
                :param skype: Handle to Skype4Py instance
                """
 
                logger.debug('test handler init')
 
                self.skype = sevabot.getSkype()
                self.calls = {}
 
                self.commands = {'test': self.test,}
 
                # maybe move this to another class, to avoid cluttering this one?
                # could be something like
                # self.callbacks = Functions().get_callback_dict()
                # or something along the lines of that
                self.callbacks = {
                        '!uptime' : self.uptime,
                        'teststateful' : self.test,
                        '!kickfelipe' : self.kickfelipe,
                        '!testformat' : self.testformat,
                        '!markov' : self.doMarkov
                        '^' : self.agree,
                        'nice!' : self.nice,
                        '!sp' : self.sp
                }
               
                self.markovGen = Markov()
 
        def handle_message(self, msg, status):
                """
                Override this method to customize a handler.
                """
                body = ensure_unicode(msg.Body)
 
                logger.debug('test handler got: {}'.format(body))
 
                # If the separators are not specified, runs of consecutive
                # whitespace are regarded as a single separator
                words = body.split()
 
                if not len(words):
                        return False
 
                #if words[0] != 'teststateful':
                #       return False
 
                try:
                        args = words[1:]
                        if words[0] != "!sp" and self.spState == True:
                                return True
                        if msg.FromHandle = 'alchemisbot':
                                return False
                        try:
                                if words[0] in self.callbacks.keys():
                                        self.callbacks[words[0]](msg, status, args)
                                        return True
                                else:
                                        # do markov training before passing message handling to another module
                                        if not words[0].startswith('!'):
                                                self.markov.add_words(words)
                                        # ready to pass it on.
                                        return False
                        except Exception, e:
                                msg.Chat.SendMessage(str(Exception))
                                msg.Chat.SendMessage(str(traceback.format_exc()))
                                pass
                except Exception, err:
                        msg.Chat.SendMessage(str(Exception))
                        msg.Chat.SendMessage(str(traceback.format_exc()))
                        return False
                #
 
                #if not len(args):
                        # !call simply starts a call
                #       self.test(msg, status, args)
                #       return True
 
                #for name, cmd in self.commands.items():
                #       if name == args[0]:
                #               cmd(msg, status, args)
                #               return True
 
 
 
        def shutdown():
                """
                Called when the module is reloaded.
                """
                logger.debug('test handler shutdown')
               
        def doMarkov(self, msg, status, args):
                #msg.Chat.SendMessage(self.markov.gen_random_sentence())
				pass
        def sp(self, msg, status, args):
               
                if self.isAuth(msg.FromHandle) >= 2:
                        if self.spState == 0:
                                self.spState = 1
                                msg.Chat.SendMessage('/me is going to sleep...')
                        else:
                                self.spState = 0
                                msg.Chat.SendMessage('/me woke up!')
                else:
                        msg.Chat.SendMessage("You're not authorized to use this command.")
                        return False
                       
        def isAuth(self,username):
                with open("/home/skype/authList") as file:
                        auths = json.load(file)
                if username not in auths: return 0
                else: return auths[username]
       
        def nice(self, msg, status, args):
                msg.Chat.SendMessage('nice!!')
 
        def agree(self, msg, status, args):
                # Just agree to what I just said, please.
                #msg.Chat.SendMessage('I agree!')
                return False
        def test(self, msg, status, args):
                """
                Show help message to the sender.
                """
                #msg.Chat.SendMessage("{}, test succesful.").format(sharedVars.alias)
                #msg.Chat.SendMessage(os.getcwd())
                #sys.path = list("")
                #sys.path.append("/home/skype/sevabot/modules")
                msg.Chat.SendMessage("{} is testing.".format(str(msg.Sender.FullName)))
 
       
        def uptime(self, msg, status, args):
                uptime = subprocess.check_output(["uptime"])
                msg.Chat.SendMessage(str(uptime))
               
        def kickfelipe(self, msg, status, args):
                if str(msg.Chat.MyRole) == "MASTER":
                        msg.Chat.Kick("fmorisan")
                        sleep(1)
                        for user in self.skype.Friends:
                                if user.Handle == "fmorisan":
                                        msg.Chat.AddMembers(user)
                else: msg.Chat.SendMessage("I'm not authorized to do that!")
                       
        def testformat(self, msg, status, args):
                msg.Chat.SendMessage("*bold*")
               
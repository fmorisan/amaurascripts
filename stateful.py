#!/sevabot
import datetime
from sevabot.bot.stateful import StatefulSkypeHandler
from sevabot.utils import ensure_unicode


class StatefulHandler(StatefulSkypeHandler):
	def __init__(self):
		pass
	def __init__(self, sevabot):
		self.sevabot = sevabot
		self.skype = sevabot.getSkype()
		self.commands = {}
		self.timeoutDelay = datetime.timedelta(seconds=6)
		# user list is in the form of {username: [last_msg_datetime, strikes]}
		self.userList = {}
	def handle_message(self, msg, status):
		content = ensure_unicode(msg.Body).split()
		# check for spammers here
		if msg.Sender in self.userList:
			if msg.Datetime - self.userList[msg.Sender][0] < self.timeoutDelay:
				strikes = self.userList[msg.Sender][1]
				if strikes == 6:
					# RIP
					msg.Chat.SendMessage('/kick', msg.Sender)
				elif strikes in [4, 5]:
					# INCOMING
					msg.Chat.SendMessage('Stop spamming, you might be kicked!')
					self.userList[msg.Sender][1] += 1
			else:	
				# timeout period has passed, reset their strikes
				self.userList[msg.Sender] = [msg.Datetime, 0]
		else:
			self.userList[msg.Sender] = [msg.Datetime, 0]
		if msg.Sender == 'fmorisan' and content[0] == "test":
			msg.SendMessage("test")
		args = content[1:]
		for name, cmd in self.commands.items():
			if name == args[0]:
				cmd(msg, status, args)
				return True
			else:
				return False

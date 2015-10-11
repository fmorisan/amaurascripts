import sharedVars
import json


def helpText():
	print "Avaliable commands:"
	print "!pp : Displays your pp"
	print "!shop [buy|inventory|list] [item] : Buy items at the shop!"
	print "!playosu [aon] : Changes your pp by a random amount, aon mode is \"all or nothing\", which will double your pp or make you lose it all."
	print "!boost (amount) (username) : Gives the user specified an amount of pp, costs an extra {}pp to use".format(sharedVars.boostCost)
	print "!buykick (username) : Kicks specified user, costs {} pp".format(sharedVars.kickCost)
	print "WARNING: if you misspell the username on !buykick it'll charge you anyway."
	
def register(username, pp):
	with open(sharedVars.ppPath, "w") as ppFile:
		pp[username] = sharedVars.basePp
		json.dump(pp,ppFile,indent=1)
		print "Welcome to osu! You have been registered automatically, and {} have been added to your account. You can obtain more by playing osu (!playosu) or by begging other people to give you some!".format(sharedVars.basePp)
		return
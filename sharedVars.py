#v0.2 last modified by mori
#added os.path.expanduser() statements for portability, sice we're
#already importing the 'os' module
import os


boostCost = 10
kickCost = 3000
basePp = 100

shopPath = "shop"
inventoryPath = "inventory"
shopPath = os.path.expanduser("~/shop")
inventoryPath = os.path.expanduser("~/inventory")


username = os.environ["SKYPE_USERNAME"]
#username = "euphoricradioactivity"
alias = os.environ["SKYPE_FULLNAME"]
#alias = "dan"
ppPath = os.path.expanduser("~/pp")
#ppPath ="pp"
authorizedPath = os.path.expanduser("~/authList")
#authorizedPath = "authList"	
faq2Path = os.path.expanduser("~/faq")
#faq2Path = "faq"

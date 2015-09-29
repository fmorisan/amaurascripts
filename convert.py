#!/usr/bin/env python
import urllib
import json
import sys

try:
	args = sys.argv[1:]
	if len(args) == 3:
		if "btc" in args:
			jj = urllib.urlopen("https://bitpay.com/api/rates")
			bitcoinjs = jj.read()
			jj.close()
			bitcoinjs = json.loads(bitcoinjs)
			bitcoinxUSD = bitcoinjs[1]['rate']
			asked_for_bitcoin = True
		else:
			asked_for_bitcoin = False
			bitcoinxUSD = None

		n = float(args[0])
		exchange_from = args[1].upper()
		exchange_to = args[2].upper()

		if asked_for_bitcoin and exchange_from == "BTC":
			exchange_from = "USD"
			frombtc = True
		elif asked_for_bitcoin:
			exchange_to = "USD"
			frombtc = False

		url = "https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20yahoo.finance.xchange%20where%20pair%20in%20(%22{}{}%22)&format=json&env=store://datatables.org/alltableswithkeys&callback=".format(exchange_from, exchange_to)
		url = urllib.urlopen(url)
		result = url.read()
		url.close()
		result = json.loads(result)
		exchange_rate = float(result['query']['results']['rate']['Rate'])
		failed = exchange_rate == 0
		if not asked_for_bitcoin:
			if not failed:
				print "{} {} is worth {} {}".format(n, exchange_from, n*exchange_rate, exchange_to)
			else: 
				print "Specified currency not found. Please use ISO denomination."
				print "See http://bit.ly/1LENuen for more info."
		else: #they asked fot it
			if frombtc:
				print "{} BTC is worth {} {}".format(n, n*bitcoinxUSD*exchange_rate, exchange_to)
			else:
				print "{} {} is worth {} BTC".format(n, exchange_from, n*exchange_rate*(1/bitcoinxUSD))
	else:
		raise Exception("Not enough arguments.")
except Exception, e:
	print "Error: *",e,"*"
	print "Usage: !convert [amount] [base currency] [other currency]"


def calcArbitrage(usdToEuro, euroToGbp, gbpToUsd):
	initialSum = 100000
	afterChanges =  initialSum/usdToEuro/euroToGbp/gbpToUsd

	if (afterChanges > initialSum):
		arbitrage = afterChanges - initialSum
		arbitrage = int(round(arbitrage))
		return arbitrage
	return 0

n = int(raw_input())



for i in xrange(n):
	data = [ double(x) for x in raw_input().split(' ') ]
	print calcArbitrage(data[0], data[1], data[2])

	# print calcArbitrage(1.1837, 1.3829, 0.6102)	

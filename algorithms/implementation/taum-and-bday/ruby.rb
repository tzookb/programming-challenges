
def calc(blackPrice, whitePrice, blacksNeeded, whitesNeeded, transformCost)
	totalPrice = 0

	if blackPrice > whitePrice + transformCost
		totalPrice += blacksNeeded*(whitePrice+transformCost)
	else
		totalPrice += blacksNeeded*blackPrice
	end

	if whitePrice > blackPrice + transformCost
		totalPrice += whitesNeeded*(blackPrice+transformCost)
	else
		totalPrice += whitesNeeded*whitePrice
	end

	return totalPrice
end

numOfTests = gets.strip.to_i

1.upto(numOfTests) do |n|  

	numOfBlacks, numOfWhites = gets.strip.split(' ').map(&:to_i)

	priceOfBlack, priceOfWhite, transCost = gets.strip.split(' ').map(&:to_i)
	
	print calc(priceOfBlack, priceOfWhite, numOfBlacks, numOfWhites, transCost)

end
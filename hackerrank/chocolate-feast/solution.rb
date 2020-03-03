
def getTotalChockolates(cash, price, pkgsPerGift)
	chocolates = 0

	chocolates += (cash/price).floor

	wrapers = chocolates

	while wrapers/pkgsPerGift.floor > 0
		freePcks = wrapers/pkgsPerGift.floor
		chocolates += freePcks
		wrapers = wrapers - freePcks*pkgsPerGift
		wrapers += freePcks
	end

	return chocolates
end

numOfTests = gets().strip.to_i

1.upto(numOfTests) do |x|
	cash, price, pkgsPerGift = gets().strip.split(" ").map(&:to_i)
	puts getTotalChockolates(cash, price, pkgsPerGift)
end
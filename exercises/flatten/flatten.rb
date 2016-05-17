def flatten(multArr)
	flattened = []
	multArr.each do |item|
		if item.kind_of?(Array)
			item = flatten(item)
		else
			item = [item]
		end
		flattened = flattened+item
	end
	return flattened.uniq
end
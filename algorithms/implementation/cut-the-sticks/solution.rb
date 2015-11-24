sticks = [5, 4, 4, 2, 2, 8]
gets()
sticks = gets().strip.split(" ").map(&:to_i)


continueCutting = true

while continueCutting do 
	continueCutting = false
	min = sticks.min
	cuttedSticks = 0
	tempSticks = sticks
	sticks = []
	
	#print tempSticks

	tempSticks.each_with_index do |x, i|
		x -= min
		cuttedSticks += 1
		if x > 0
			sticks.push(x)			
				
			continueCutting = true
		
		end
	end

	puts cuttedSticks

	
	#gets()
	
end

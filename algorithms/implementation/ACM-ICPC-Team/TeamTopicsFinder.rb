class TeamTopicsFinder
	
	@maxAmountOfTopics = -1
	@countCouplesWhoKnowsMostTopics = 0


	def getNumberOfOnesInBinaryString(binaryStr)	
		binaryStr.split('').map(&:to_i).reduce(:+)
	end

	def getIntegerValueFromBinaryString(binaryString)
		
		binaryString.to_i(2)
	end

	def getBinaryStringFromInteger(number)
		number.to_s(2)
	end

	def andTwoIntegers(int1, int2)
		int1&int2
	end

	def orTwoIntegers(int1, int2)
		int1|int2
	end

	def getMergedArrayOfUsersTopics(topicsArr1, topicsArr2)
		topicsArr1 = topicsArr1.split
		topicsArr2 = topicsArr2.split

		topicsArr1.zip(topicsArr2).map { |x, y| x.to_i + y.to_i }
	end


	def getTopicsKnownInArray(topicsArr)
		topicsArr.select {|e| e > 0}.size
	end


	def handleTotalTopics(totalTopics)
		if totalTopics > @maxAmountOfTopics
			@maxAmountOfTopics = totalTopics
			@countCouplesWhoKnowsMostTopics = 1
		elsif totalTopics == @maxAmountOfTopics
			@countCouplesWhoKnowsMostTopics += 1
		end
	end


	def checkUserWithOtherUsers(currentUserTopics, currentUserIndex, amountOfUsers, knowledgeArr)
		(currentUserIndex+1).upto(amountOfUsers-1) do |otherUserIndex|

			otherUserKnowledge = self.getIntegerValueFromBinaryString(knowledgeArr[otherUserIndex])
			
			#puts currentUserTopics
			#puts otherUserKnowledge
			
			mergedKnoweledges = self.orTwoIntegers(currentUserTopics, otherUserKnowledge)

			#puts mergedKnoweledges

			totalKnoweledges = self.getNumberOfOnesInBinaryString(self.getBinaryStringFromInteger(mergedKnoweledges))

			#puts totalKnoweledges
			

			self.handleTotalTopics(totalKnoweledges)
			
		end
	end


	def boom(amountOfUsers, knowledgeArr)
		
		@maxAmountOfTopics = -1
		@countCouplesWhoKnowsMostTopics = 0


		0.upto(amountOfUsers-1) do |userIndex|
	
			userKnowledge = self.getIntegerValueFromBinaryString(knowledgeArr[userIndex])

			self.checkUserWithOtherUsers(userKnowledge, userIndex, amountOfUsers, knowledgeArr)
			
		end

		return @maxAmountOfTopics, @countCouplesWhoKnowsMostTopics
	end

end
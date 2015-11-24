class TeamTopicsFinder
	
	@@maxAmountOfTopics = -1
	@countCouplesWhoKnowsMostTopics = 0

	
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

			otherUserKnowledge = knowledgeArr[otherUserIndex]
			
			mergedKnoweledges = self.getMergedArrayOfUsersTopics(currentUserTopics, otherUserKnowledge)

			totalKnoweledges = self.getTopicsKnownInArray(mergedKnoweledges)

			self.handleTotalTopics(totalKnoweledges)
			
		end
	end


	def boom(amountOfUsers, knowledgeArr)
		
		@maxAmountOfTopics = -1
		@countCouplesWhoKnowsMostTopics = 0


		0.upto(amountOfUsers-1) do |userIndex|
	
			userKnowledge = knowledgeArr[userIndex]

			self.checkUserWithOtherUsers(userKnowledge, userIndex, amountOfUsers, knowledgeArr)
			
		end

		return @maxAmountOfTopics, @countCouplesWhoKnowsMostTopics
	end

end
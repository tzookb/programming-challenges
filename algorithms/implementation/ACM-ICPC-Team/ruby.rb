

team = TeamTopicsFinder.new


amountOfUsers, amountOfTopics = gets.split(' ').map(&:to_i)

knowledgeArr = []


1.upto(amountOfUsers) do
	arr = gets.strip   #.split('').map(&:to_i)
	knowledgeArr.push(arr)
end


maxAmountOfTopics, countCouplesWhoKnowsMostTopics = team.boom(amountOfUsers, knowledgeArr)




puts maxAmountOfTopics
puts countCouplesWhoKnowsMostTopics
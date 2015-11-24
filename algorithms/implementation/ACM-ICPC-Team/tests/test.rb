require_relative "../TeamTopicsFinder.rb"
require "test/unit"
 
class TestSimpleNumber < Test::Unit::TestCase
 
  def test_simple
    team = TeamTopicsFinder.new

    amountOfUsers = 500
    amountOfTopics = 500
    
    file = File.open("input1.txt", "rb")
	contents = file.read

	userTopics = contents.split("\n")


	maxAmountOfTopics, countCouplesWhoKnowsMostTopics = team.boom(amountOfUsers, userTopics)

	

	puts maxAmountOfTopics
	puts countCouplesWhoKnowsMostTopics

  end
 
end
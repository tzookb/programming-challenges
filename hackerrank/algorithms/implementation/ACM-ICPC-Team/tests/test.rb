require_relative "../TeamTopicsFinder.rb"
require "test/unit"
 
class TestSimpleNumber < Test::Unit::TestCase
 
    def test_create_Instance
        team = TeamTopicsFinder.new 
        assert_equal('TeamTopicsFinder', team.class.name)
    end

    def test_getNumberOfOnesInBinaryString
        team = TeamTopicsFinder.new 
        
        assert_equal(3, team.getNumberOfOnesInBinaryString('100011')) 
    end

    def test_check_integer_to_binary_string
        team = TeamTopicsFinder.new 
        
        assert_equal('100', team.getBinaryStringFromInteger(4)) 
        assert_equal('1111', team.getBinaryStringFromInteger(15))
    end

    def test_check_binary_str_to_integer
        team = TeamTopicsFinder.new 
        
        assert_equal(1, team.getIntegerValueFromBinaryString('1'))
        assert_equal(3, team.getIntegerValueFromBinaryString('11'))
        assert_equal(4, team.getIntegerValueFromBinaryString('100'))
        assert_equal(15, team.getIntegerValueFromBinaryString('1111')) 
    end

    def test_take_2_numbers_and_AND_them_together
        team = TeamTopicsFinder.new 
        
        assert_equal(1, team.andTwoIntegers(1, 3))
        assert_equal(0, team.andTwoIntegers(3, 4))
    end

    def test_take_2_numbers_and_OR_them_together
        team = TeamTopicsFinder.new 
        assert_equal(5, team.orTwoIntegers(1, 4)) 
        assert_equal(7, team.orTwoIntegers(3, 4))
    end


    def test_simple
        team = TeamTopicsFinder.new

        amountOfUsers = 3
        amountOfTopics = 3
        
        file = File.open("input1.txt", "rb")
        contents = file.read

        userTopics = ['110','101','101']


        maxAmountOfTopics, countCouplesWhoKnowsMostTopics = team.boom(amountOfUsers, userTopics)

        assert_equal(3, maxAmountOfTopics) 
        assert_equal(2, countCouplesWhoKnowsMostTopics)
        
     end

     def test_simple2
        team = TeamTopicsFinder.new

        amountOfUsers = 4
        amountOfTopics = 3
        
        file = File.open("input1.txt", "rb")
        contents = file.read

        userTopics = ['110','101','100', '000']


        maxAmountOfTopics, countCouplesWhoKnowsMostTopics = team.boom(amountOfUsers, userTopics)

        assert_equal(3, maxAmountOfTopics) 
        assert_equal(1, countCouplesWhoKnowsMostTopics)
        
     end

    
    def test_big
        puts Time.now
        team = TeamTopicsFinder.new

        amountOfUsers = 500
        amountOfTopics = 500
        
        file = File.open("input1.txt", "rb")
        contents = file.read

        userTopics = contents.split("\n")


        maxAmountOfTopics, countCouplesWhoKnowsMostTopics = team.boom(amountOfUsers, userTopics)

        puts Time.now

        puts maxAmountOfTopics
        puts countCouplesWhoKnowsMostTopics

     end
 
end
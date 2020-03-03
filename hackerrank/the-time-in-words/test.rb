require_relative "ruby.rb"
require "test/unit"
 
class TestSimpleNumber < Test::Unit::TestCase
 
  def test_creation
  	obj = TimeInToWords.new
  end

  def test_5_00
  	obj = TimeInToWords.new
  	strTime = obj.getTimeInStr('5:00')
  	assert_equal('five o`clock', strTime)
  end

  def test_6_00
  	obj = TimeInToWords.new
  	strTime = obj.getTimeInStr('6:00')
  	assert_equal('six o`clock', strTime)
  end

  def test_12_00
  	obj = TimeInToWords.new
  	strTime = obj.getTimeInStr('12:00')
  	assert_equal('twelve o`clock', strTime)
  end

  def test_3_30
  	obj = TimeInToWords.new
  	strTime = obj.getTimeInStr('3:30')

  	assert_equal('half past three', strTime)
  end

  def test_11_30
  	obj = TimeInToWords.new
  	strTime = obj.getTimeInStr('11:30')
  	assert_equal('half past eleven', strTime)
  end

  def test_NumToStr_5
  	numToStr = NumberToString.new
  	assert_equal('five', numToStr.getStringOfNumber(5))
  	assert_equal('thirteen', numToStr.getStringOfNumber(13))
  end
 
end
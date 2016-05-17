require './flatten'
require 'minitest/autorun'

class StringTest < Minitest::Test

  def test_simple_mult
    res = flatten([1,2,[2,3],4])
    assert_equal([1,2,3,4], res)
  end

  def test_simple
    res = flatten([1,2,4])
    assert_equal([1,2,4], res)
  end

  def test_simple_with_duplicates
    res = flatten([1,2,4,2,4])
    assert_equal([1,2,4], res)
  end

  def test_2_level_arr
    res = flatten([1,2,3,[1,[2,3]]])
    assert_equal([1,2,3], res)
  end

  def test_many_level_arr
    res = flatten([1,2,3,[1,[2,[2,[3,[3,4,[5]]]]]]])
    assert_equal([1,2,3,4,5], res)
  end

  def test_empty_arr
    res = flatten([])
    assert_equal([], res)
  end

  def test_empty_inner_arr
    res = flatten([[[[]]]])
    assert_equal([], res)
  end

  def test_single
    res = flatten([1])
    assert_equal([1], res)
  end

end
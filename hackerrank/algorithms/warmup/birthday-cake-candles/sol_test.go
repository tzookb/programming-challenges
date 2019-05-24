package main

import "testing"

func TestNewDeck(t *testing.T) {
	res := birthdayCakeCandles([]int32{2, 3, 1, 3})
	if res != 2 {
		t.Errorf("Expected length max to be: %v", res)
	}

	resa := birthdayCakeCandles([]int32{2, 3, 2, 2, 3})
	if resa != 2 {
		t.Errorf("Expected lengtha max to be: %v", res)
	}
}

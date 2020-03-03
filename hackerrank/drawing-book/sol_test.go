package main

import "testing"

func TestPageCount(t *testing.T) {

	out := pageCount(6, 5)
	if out != 1 {
		t.Errorf("6,5 exp 1: %v", out)
	}
	if pageCount(7, 6) != 0 {
		t.Errorf("7,6 exp 0")
	}
	if pageCount(7, 7) != 0 {
		t.Errorf("7,7 exp 0")
	}
	if pageCount(6, 6) != 0 {
		t.Errorf("6,6 exp 0")
	}
	if pageCount(6, 1) != 0 {
		t.Errorf("6,1 exp 0")
	}
	if pageCount(6, 2) != 1 {
		t.Errorf("6,2 exp 1")
	}
	if pageCount(5, 4) != 0 {
		t.Errorf("5,4 exp 0")
	}
}

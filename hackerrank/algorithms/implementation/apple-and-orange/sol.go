package main

import "fmt"

func main() {
	var leftHome int32 = 7
	var righttHome int32 = 11
	var appleLoc int32 = 5
	var orangeLoc int32 = 15
	apples := []int32{-2, 2, 1}
	oranges := []int32{5, -6}
	countApplesAndOranges(leftHome, righttHome, appleLoc, orangeLoc, apples, oranges)
}

func countApplesAndOranges(homeLeft int32, homeRight int32, appleLoc int32, orangeLoc int32, apples []int32, oranges []int32) {
	applesInHome := 0
	orangesInHome := 0

	for _, apple := range apples {
		fallenAppleLoc := appleLoc + apple
		if fallenAppleLoc >= homeLeft && fallenAppleLoc <= homeRight {
			applesInHome++
		}
	}
	for _, orange := range oranges {
		fallenOrangeLoc := orangeLoc + orange
		if fallenOrangeLoc >= homeLeft && fallenOrangeLoc <= homeRight {
			orangesInHome++
		}
	}
	fmt.Println(applesInHome)
	fmt.Println(orangesInHome)
}

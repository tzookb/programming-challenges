package main

import (
	"fmt"
)

func main() {
	people := []int32{1, 2}
	res := fairRations(people)
	fmt.Println(res)
}

// hackerRank has an issue in this exercise...
// they want me to return a string
// from a func that suppose to return an int32
func fairRations(B []int32) int32 {
	var rations int32
	i := 0
	for i < len(B) {
		cur := B[i]
		if cur%2 == 0 {
			i++
			continue
		}
		B[i]++
		if i == len(B)-1 {
			//we are in the end so not possible to ration
			fmt.Println("NO")
			return B[i]
		}
		B[i+1]++
		rations += 2
		i++
	}
	fmt.Println(rations)
	return rations
}

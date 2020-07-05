package main

import (
	"fmt"
)

func main() {
	candles := []int32{2, 3, 1, 3}
	res := birthdayCakeCandles(candles)
	fmt.Println(res)
}

func birthdayCakeCandles(ar []int32) int32 {
	mappings := map[int32]int32{}
	for _, val := range ar {
		_, err := mappings[val]
		if !err {
			mappings[val] = 0
		}
		mappings[val]++
	}

	var max int32
	for key := range mappings {
		if key > max {
			max = key
		}
	}
	return mappings[max]
}

package main

import (
	"fmt"
)

func main() {
	arr := []int32{1, 4, 4, 4, 5, 3}
	res := migratoryBirds(arr)
	fmt.Println(res)
}

func migratoryBirds(arr []int32) int32 {
	counts := make(map[int32]int)
	for _, num := range arr {
		if _, ok := counts[num]; !ok {
			counts[num] = 0
		}
		counts[num]++
	}
	var maxVal int
	for _, num := range counts {
		if num > maxVal {
			maxVal = num
		}
	}

	var maxKey int32 = 999999999
	for key, val := range counts {
		if val == maxVal {
			if key < maxKey {
				maxKey = key
			}
		}
	}
	return maxKey
}

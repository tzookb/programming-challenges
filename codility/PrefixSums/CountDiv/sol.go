package main

import (
	"fmt"
	"math"
)

func main() {
	res := Solution(6, 11, 2)
	fmt.Println(res)
}

func Solution(A int, B int, K int) int {
	// floor(B/k) - ceil(A/K) + 1
	left := math.Floor(float64(B) / float64(K))
	right := math.Ceil(float64(A) / float64(K))
	return int(left - right + 1)
}

package main

import (
	"math"
)

func main() {
	pageCount(6, 5)
}

func pageCount(n int32, p int32) int32 {
	left := float64(math.Floor(float64(p / 2)))
	var right float64

	if n%2 == 0 {
		right = math.Ceil(float64(float64(n)-float64(p)) / 2)
	} else {
		right = float64(math.Floor(float64((n - p) / 2)))
	}
	minPageTurned := math.Min(left, right)
	return int32(minPageTurned)
}

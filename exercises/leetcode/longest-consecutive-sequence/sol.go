package main

import (
	"math"
)

func main() {
	nums := []int{100, 4, 200, 1, 3, 2}

	longestConsecutive(nums)
}

func longestConsecutive(nums []int) int {
	mapped := make(map[int]bool)
	for _, val := range nums {
		mapped[val] = true
	}
	max_streak := 0

	for num := range mapped {
		prev := num - 1
		if _, ok := mapped[prev]; ok {
			continue
		}
		streak := 0
		cur := num
		for {
			if _, ok := mapped[cur]; !ok {
				break
			}
			cur += 1
			streak += 1
		}
		max_streak = int(math.Max(float64(streak), float64(max_streak)))
	}

	return max_streak
}

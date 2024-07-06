package main

import (
	"fmt"
	"math"
	"slices"
)

func main() {
	nums := []int{1, 5, 0, 10, 14}

	res := minDifference(nums)
	fmt.Println(res)
}

func minDifference(nums []int) int {
	slices.Sort(nums)
	minDiff := int(math.Inf(1))

	for i := range 4 {
		fmt.Println(i)
		math.Min(minDiff, nums[i]-nums[i])
	}

	return nums[0]
}

package main

import (
	"fmt"
	"sort"
)

func main() {
	keyboards := []int32{3, 1}
	usbs := []int32{5, 2, 8}
	res := getMoneySpent(keyboards, usbs, 10)
	fmt.Println(res)
}

type result struct {
	sum      int32
	keyboard int32
	drive    int32
}

func getMoneySpent(k []int32, d []int32, b int32) int32 {

	sort.Slice(k, func(i, j int) bool {
		return k[i] < k[j]
	})
	sort.Slice(d, func(i, j int) bool {
		return d[i] < d[j]
	})

	var maxSum int32

	for _, valK := range k {
		for _, valD := range d {
			sum := valK + valD
			if sum > b {
				break
			}
			if sum > maxSum {
				maxSum = sum
			}
		}
	}
	if maxSum > 0 {
		return maxSum
	}
	return -1
}

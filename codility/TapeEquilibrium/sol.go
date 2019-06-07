package main

import (
	"fmt"
	"math"
	"sort"
)

func main() {
	arr := []int{3, 1, 2, 4, 3}
	res := Solution(arr)
	fmt.Println(res)
}

func Solution(A []int) int {
	ls := make([]int, len(A))
	rs := make([]int, len(A))
	for i := range A {
		ls[i] = A[i]
		if i > 0 {
			ls[i] += ls[i-1]
		}
		oi := len(A) - 1 - i
		rs[oi] = A[oi]
		if oi < len(A)-1 {
			rs[oi] += rs[oi+1]
		}
	}
	sums := []int{}
	for i := 0; i < len(ls)-1; i++ {
		sums = append(sums,
			int(math.Abs(float64(ls[i]-rs[i+1]))),
		)
	}
	sort.Ints(sums)
	return sums[0]
}

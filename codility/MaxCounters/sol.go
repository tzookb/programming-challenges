package main

import "fmt"

func main() {
	a := []int{3, 4, 4, 6, 1, 4, 4}
	x := 5
	res := Solution(x, a)
	fmt.Println(res)
}

func Solution(N int, A []int) []int {
	counters := make([]int, N)
	var max int
	var forcedVal int

	for _, v := range A {
		if v > N {
			forcedVal = max
		} else {
			cur := counters[v-1]
			if cur < forcedVal {
				cur = forcedVal
			}
			cur++
			if cur > max {
				max = cur
			}
			counters[v-1] = cur
		}
	}
	for i := range counters {
		if counters[i] < forcedVal {
			counters[i] = forcedVal
		}
	}
	return counters
}

package main

import "fmt"

func main() {
	arr := []int{9, 3, 9, 3, 9, 7, 9}
	res := Solution(arr)
	fmt.Println(res)
}

func Solution(A []int) int {
	counts := map[int]int{}

	for _, v := range A {
		if _, ok := counts[v]; ok {
			delete(counts, v)
		} else {
			counts[v] = 1
		}
	}

	var leftVal int
	for k := range counts {
		leftVal = k
		break
	}

	return leftVal
}

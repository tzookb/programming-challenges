package main

import "fmt"

func main() {
	// arr := []int{1, 3, 6, 4, 1, 2}
	arr := []int{-2, -1}
	res := Solution(arr)
	fmt.Println(res)
}

func Solution(A []int) int {
	min := 1
	items := make(map[int]bool)

	for _, v := range A {
		items[v] = true
	}

	for {
		_, ok := items[min]
		if !ok {
			return min
		}
		min++
	}
}

package main

import "fmt"

func main() {
	a := []int{4, 1, 3}
	res := Solution(a)
	fmt.Println(res)
}

func Solution(A []int) int {
	items := map[int]bool{}

	for idx := range A {
		items[idx+1] = false
	}
	for _, val := range A {
		items[val] = true
	}
	for _, v := range items {
		if !v {
			return 0
		}
	}

	return 1
}

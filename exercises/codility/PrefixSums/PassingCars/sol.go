package main

import "fmt"

func main() {
	arr := []int{0, 1, 0, 1, 1}
	res := Solution(arr)
	fmt.Println(res)
}

func Solution(A []int) int {
	totalPassing := 0
	curSum := 0

	for i := len(A) - 1; i >= 0; i-- {
		if A[i] == 1 {
			curSum++
		} else {
			totalPassing += curSum
			if totalPassing > 1000000000 {
				return -1
			}
		}
	}
	return totalPassing
}

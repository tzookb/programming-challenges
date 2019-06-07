package main

import (
	"fmt"
)

func main() {
	arr := []int{1, 2, 3, 4, 5, 6, 7, 8}
	k := 3
	res := Solution(arr, k)
	fmt.Println(res)
}

func Solution(A []int, K int) []int {
	arrLen := len(A)
	if arrLen == 0 {
		return A
	}
	moves := K % arrLen

	return append(
		A[arrLen-moves:arrLen],
		A[0:arrLen-1]...,
	)
}

package main

import (
	"fmt"
)

func main() {
	arr := []int{}
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
	copiedA := A[:]
	for i := 0; i < moves; i++ {
		copiedA = append(copiedA[arrLen-1:], copiedA[:arrLen-1]...)
	}
	return copiedA
}

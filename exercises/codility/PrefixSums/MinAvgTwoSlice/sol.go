package main

import "fmt"

func main() {
	arr := []int{4, 2, 2, 5, 1, 5, 8}
	res := Solution(arr)
	fmt.Println(res)
}

func Solution(A []int) int {
	var minVal float64 = 10001
	minIdx := 0
	for i := 0; i < len(A)-1; i++ {
		first := A[i]
		sec := A[i+1]
		avg := float64(float64(first+sec) / float64(2))
		if avg < minVal {
			minVal = avg
			minIdx = i
		}
		if i < len(A)-2 {
			// size 3 check
			third := A[i+2]
			avg := float64(float64(first+sec+third) / float64(3))
			if avg < minVal {
				minVal = avg
				minIdx = i
			}
		}
	}
	return minIdx
}

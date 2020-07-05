package main

import "fmt"

func main() {
	arr := []int{1, 2, 3, 5}
	res := Solution(arr)
	fmt.Println(res)
}

func Solution(A []int) int {
	var sum int
	var aSum int
	for idx, v := range A {
		sum += idx + 1
		aSum += v
	}
	sum += len(A) + 1

	return sum - aSum
}

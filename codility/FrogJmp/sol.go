package main

import (
	"fmt"
	"math"
)

func main() {
	res := Solution(10, 85, 30)
	fmt.Println(res)
}

func Solution(X int, Y int, D int) int {
	return int(math.Ceil(float64(Y-X) / float64(D)))
}

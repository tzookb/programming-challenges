package main

import (
	"fmt"
	"math"
)

func main() {
	arr := []int32{1, 2, 5, 3, 7, 8, 6, 4}
	// arr := []int32{1, 2, 3, 4, 5, 6, 7, 8}
	// arr := []int32{1, 2, 5, 3, 4, 6, 7, 8}
	// arr := []int32{1, 2, 5, 3, 7, 4, 6, 8}
	// arr := []int32{1, 2, 5, 3, 7, 8, 4, 6}
	// arr := []int32{1, 2, 5, 3, 7, 8, 6, 4}
	minimumBribes(arr)

}

func minimumBribes(q []int32) {
	var bribes float64

	for pos := len(q)-1; i >= 0; i-- {
		curSpot = q[pos]
		realpos := pos + 1
		diffFromSpot := math.Abs(float64(int32(realpos) - curSpot))

		if curSpot - realpos > 2 {
			fmt.Println("Too chaotic")
			return
		}
		
		for _, j
	}

        for j in range(max(0, q[i] - 2),i):
            if q[j] > q[i]:
                bribes+=1
    print(bribes)

	fmt.Println(totalDoubleBribes)
	fmt.Println(totalDoubleBribes / 2)
}

package main

import "fmt"

func main() {
	clouds := []int32{0, 0, 1, 0, 0, 1, 0}
	res := jumpingOnClouds(clouds)
	fmt.Println(res)
}

func jumpingOnClouds(c []int32) int32 {
	var jumps int32
	cidx := 0
	eidx := len(c) - 1
	for {
		if cidx == eidx {
			return jumps
		}
		twoStepIdx := cidx + 2
		cidx++
		if twoStepIdx <= eidx && c[twoStepIdx] == 0 {
			cidx++
		}
		jumps++
	}
}

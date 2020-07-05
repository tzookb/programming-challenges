package main

import (
	"fmt"
	"strconv"
	"strings"
)

func main() {
	res := solution(561892)
	fmt.Println(res)
}

func solution(num int) int {
	str := strconv.FormatInt(int64(num), 2)
	digits := strings.Split(str, "")

	canCount := false
	maxGap := 0
	curGap := 0

	for _, d := range digits {
		if d == "1" {
			canCount = true
			if curGap > maxGap {
				maxGap = curGap
			}
			curGap = 0
		} else {
			if canCount {
				curGap++
			}
		}
	}

	return maxGap
}

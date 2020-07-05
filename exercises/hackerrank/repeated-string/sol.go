package main

import (
	"fmt"
	"math"
	"strings"
)

func main() {
	s := "aba"
	var n int64 = 10
	res := repeatedString(s, n)
	fmt.Println(res)
	//findAinString("bbaaca")
}

func repeatedString(s string, n int64) int64 {
	sLen := int64(len(s))
	times := int(math.Floor(float64(n / sLen)))
	extra := int(n % sLen)
	restOfStr := s[:extra]
	return int64(findAinString(s)*times + findAinString(restOfStr))
}

func findAinString(s string) int {
	var count int
	for _, v := range strings.Split(s, "") {
		if v == "a" {
			count++
		}
	}
	return count
}

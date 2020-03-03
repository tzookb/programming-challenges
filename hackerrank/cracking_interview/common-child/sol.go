package main

import "fmt"

func main() {
	var s1 string = "HARRY"
	var s2 string = "SALLY"

	// fmt.Println(s1[0 : len(s1)-1])
	// fmt.Println(s1)

	fmt.Println(commonChild(s1, s2))
}

func Max(x, y int) int {
	if x < y {
		return y
	}
	return x
}
func commonChild(s1 string, s2 string) int {
	if len(s1) == 0 || len(s2) == 0 {
		return 0
	}

	if s1[len(s1)-1:] == s2[len(s2)-1:] {
		return 1 + commonChild(s1[0:len(s1)-1], s2[0:len(s2)-1])
	} else {
		return Max(commonChild(s1, s2[0:len(s2)-1]), commonChild(s1[0:len(s1)-1], s2))
	}
}

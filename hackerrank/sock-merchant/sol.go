package main

import "fmt"

// Complete the sockMerchant function below.
func sockMerchant(n int32, ar []int32) int32 {
	var pairs int32 = 0
	socksCounter := make(map[int32]int)

	for _, v := range ar {
		if _, ok := socksCounter[v]; !ok {
			socksCounter[v] = 0
		}
		socksCounter[v]++
	}
	for _, v := range socksCounter {
		pairs += int32(v / 2)
	}

	return pairs
}

func main() {
	var n int32 = 9
	ar := []int32{10, 20, 20, 10, 10, 30, 50, 10, 20}
	result := sockMerchant(n, ar)
	fmt.Println(result)
}

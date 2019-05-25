package main

import "fmt"

// fibonacci is a function that returns
// a function that returns an int.
func fibonacci() func() int {
	first := 0
	second := 1
	round := 1
	return func() int {
		if round == 1 {
			round++
			return 0
		}
		if round == 2 {
			round++
			return 1
		}
		result := first + second
		first = second
		second = result
		return result
	}
}

func main() {
	f := fibonacci()
	for i := 0; i < 10; i++ {
		fmt.Println(f())
	}
}

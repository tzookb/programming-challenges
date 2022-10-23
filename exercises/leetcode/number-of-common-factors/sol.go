package main

import (
	"math"
)

func main() {
	commonFactors(25, 30)
}

func commonFactors(a int, b int) int {
	counter := make(map[int]bool)
	counted := 0

	upTo := int(math.Floor(math.Sqrt(float64(a))))
	for tocheck := upTo; tocheck >= 1; tocheck-- {
		if a%tocheck > 0 {
			continue
		}
		partner := int(a / tocheck)
		counter[tocheck] = true
		counter[partner] = true
	}

	upTo = int(math.Floor(math.Sqrt(float64(b))))
	for tocheck := upTo; tocheck >= 1; tocheck-- {
		if b%tocheck > 0 {
			continue
		}
		partner := int(b / tocheck)
		if _, ok := counter[tocheck]; ok {
			counted += 1
			delete(counter, tocheck)
		}
		if _, ok := counter[partner]; ok {
			counted += 1
			delete(counter, partner)
		}
	}
	return counted
}

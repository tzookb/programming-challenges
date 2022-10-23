package main

import "fmt"

func main() {
	nums := []int{2, 7, 11, 15}
	target := 9

	res := twoSum(nums, target)
	fmt.Println(res)
}
func twoSum(nums []int, target int) []int {
	dict := make(map[int]int)
	sol := []int{}
	for idx, val := range nums {
		partnerval := target - val
		fmt.Println(val)
		if partneridx, ok := dict[partnerval]; ok {
			sol = append(sol, idx, partneridx)
			break
		}
		dict[val] = idx
	}
	return sol
}

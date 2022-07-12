package main

/**
 * Definition for singly-linked list.
 */
type ListNode struct {
	Val  int
	Next *ListNode
}

func main() {

}
func permute(nums []int) [][]int {
	var sol [][]int

	if len(nums) <= 1 {
		sol = append(sol, nums)
		return sol
	}

	for _, num := range nums {
		leftover := nums[1:]
		permute(leftover)
		for _, curnum := range leftover {
			permute()
		}
	}

	initialPerm := []int{}
	dfs(initialPerm, nums)

	return sol
}

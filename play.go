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

func reverseList(head *ListNode) *ListNode {
	if head == nil || head.Next == nil {
		return head
	}

	var prev *ListNode = head
	var cur *ListNode = head.Next
	prev.Next = nil

	for cur != nil {
		var nextCur *ListNode = cur.Next
		cur.Next = prev
		prev = cur
		cur = nextCur
	}

	return prev
}

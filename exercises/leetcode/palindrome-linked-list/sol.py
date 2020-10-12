# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow = head
        fast = head
        tillHere = []

        while fast:
            tillHere.append(slow.val)
            fast = fast.next
            slow = slow.next

            if fast:
                fast = fast.next

        left = []
        while slow:
            left.append(slow.val)
            slow = slow.next

        if len(tillHere) > len(left):
            tillHere.pop()


        return tillHere[::-1] == left
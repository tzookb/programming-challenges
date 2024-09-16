# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        fake = ListNode(None, head)
        prev = fake
        cur = head
        
        removes = {}
        for n in nums:
            removes[n] = True
        

        while cur:
            if cur.val in removes:
                prev.next = cur.next
                cur = cur.next
            else:
                prev = cur
                cur = cur.next
                
            
            

        return fake.next
        
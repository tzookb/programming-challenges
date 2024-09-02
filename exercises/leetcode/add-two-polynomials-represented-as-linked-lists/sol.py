# Definition for polynomial singly-linked list.
# class PolyNode:
#     def __init__(self, x=0, y=0, next=None):
#         self.coefficient = x
#         self.power = y
#         self.next = next

class Solution:
    def addPoly(self, poly1: 'PolyNode', poly2: 'PolyNode') -> 'PolyNode':
        if not poly1 and not poly2:
            return None
        if not poly1:
            return poly2
        if not poly2:
            return poly1
        
        curPower = max(poly1.power, poly2.power)

        fake = PolyNode()
        cur = fake
        while poly1 or poly2:
            summed = 0
            if not poly2:
                summed = poly1.coefficient
                power = poly1.power
                poly1 = poly1.next
            elif not poly1:
                summed = poly2.coefficient
                power = poly2.power
                poly2 = poly2.next
            else:
                if poly1.power == poly2.power:
                    summed = poly1.coefficient + poly2.coefficient
                    power = poly2.power
                    poly1 = poly1.next
                    poly2 = poly2.next
                elif poly1.power > poly2.power:
                    summed = poly1.coefficient
                    power = poly1.power
                    poly1 = poly1.next
                else:
                    summed = poly2.coefficient
                    power = poly2.power
                    poly2 = poly2.next

            if summed:
                summedNode = PolyNode(summed, power)
                cur.next = summedNode
                cur = cur.next

        return fake.next
        
        
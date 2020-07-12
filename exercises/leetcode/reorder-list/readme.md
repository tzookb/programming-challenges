---
title: LeetCode - reorder-list challenge solution
author: tzookb
type: post
date: 2020-07-11T09:07:08+00:00
url: /leetcode/reorder-list
desc: leetcode reorder-list exercise
source: https://leetcode.com/problems/reorder-list/
---

For this exercise I'm quite sure there is a better way of doing it, but this seemed like a nice solution.
What I did is extracting the linked list items to an array by its order.
Then I looped over the first half of the array and rearanged the pointers.
The reason I'm doing only the first half, is because on each index `i` I'll be changing its opposite index as well `n-i`.

So lets break it apart, first extracting the linked list to an array:

```
mappings = []
    item = head
    while item:
        mappings.append(item)
        item = item.next
```

Then the pointers rearranging:

```
total = len(mappings)
    upTo = math.floor(total/2)
    for i in range(upTo):
        mappings[i].next = mappings[total-1-i]
        mappings[total-1-i].next = mappings[i+1]
```

The full code:

```
def reorderList(self, head: ListNode) -> None:
    if not head or head.next == None:
        return head
    mappings = []
    item = head
    while item:
        mappings.append(item)
        item = item.next

    total = len(mappings)
    upTo = math.floor(total/2)
    for i in range(upTo):
        mappings[i].next = mappings[total-1-i]
        mappings[total-1-i].next = mappings[i+1]

    mappings[i+1].next = None

    return mappings[0]
```

Just wanted to explain the first lines, as I first check if the list is either empty or with a single element.
If so, I'll just return it as no changes will be needed.

The last 2 lines, are making sure the "middle" element will be point to None to make sure we wont have an endless loop.
And then we return our head.
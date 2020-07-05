class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None

def printList(l):
    item = l
    vals = []
    while item:
        vals.append(item.value)
        item = item.next
    print(vals)

def makeList(vals):
    vals.reverse()
    l = None
    for item in vals:
        newList = ListNode(item)
        newList.next = l
        l = newList
    return l

def reverseList(l):
    cur = l
    setNext = None
    last = None
    while cur:
        last = cur
        nextItem = cur.next
        cur.next = setNext
        setNext = cur
        cur = nextItem
    return last

def compareLists(l1, l2):
    while l1 and l2:
        if l1.value != l2.value:
            return False
        l1 = l1.next
        l2 = l2.next
    if l1 or l2:
        return False
    return True

def isListPalindrome(l):
    if not l or not l.next:
        return True
    fast = l
    slow = l
    prev_slow = l
    while slow and fast and fast.next:
        prev_slow = slow
        slow = slow.next
        fast = fast.next.next

    secPart = slow
    if fast:
        secPart = slow.next
    

    prev_slow.next = None
    firstPart = l
    secPartReversed = reverseList(secPart)

    return compareLists(firstPart, secPartReversed)

genList = makeList([0,0,1,0,0])
res = isListPalindrome(genList)
# res = reverseList(genList)
# printList(res)
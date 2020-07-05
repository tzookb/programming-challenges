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

def getLeadingZeros(v):
    addZeros = 4-len(v)
    return "0"*addZeros + v

def getNumberFromLinkedList(l):
    strNum = ''
    while l:
        val = getLeadingZeros(str(l.value))
        strNum += val
        l = l.next
    return int(strNum)

def addTwoHugeNumbers(a, b):
    aVal = getNumberFromLinkedList(a)
    bVal = getNumberFromLinkedList(b)
    total = aVal+bVal
    print(total)
    return
    totalStr = str(total)
    chunks = [int(totalStr[i:i+4]) for i in range(0, len(totalStr), 4)]
    return makeList(chunks)

a = makeList([123,4,5])
b = makeList([100, 100, 100])
res = addTwoHugeNumbers(a,b)
# printList(res)
# print(getLeadingZeros('21'))


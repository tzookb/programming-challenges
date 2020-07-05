def printBin(v):
    print("{0:b}".format(v))

def getBit(v, i):
    mask = 1 << i
    return (v & mask) != 0

def setBit(v, i):
    mask = 1 << i
    return v | mask

def clearBit(v, i):
    mask = ~(1 << i)
    return v & mask

def updateBit(v, i, bv):
    if bv:
        return setBit(v, i)
    return clearBit(v, i)

def getDiff(a, b):
    diff = a ^ b
    cnt = 0
    while diff > 0:
        isOne = diff & 1
        if isOne:
            cnt += 1
        diff = diff >> 1
        printBin(diff)
    return cnt

x = 12
y = 10
z = x ^ y
printBin(x)
printBin(y)
printBin(z)
print(getDiff(x, y))


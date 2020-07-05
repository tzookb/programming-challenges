def rotateImage(a):
    size = len(a)
    layers = int(size/2)
    l = 0

    while l < layers:
        first = l
        last = size - 1 - l
        i=first
        while i < last:
            offset = i - first
            
            top = a[first][i]
            a[first][i] = a[last-offset][first]
            a[last-offset][first] = a[last][last-offset]
            a[last][last-offset] = a[i][last]
            a[i][last] = top
            i += 1
        l += 1

    return a


a = [
    [ 1, 2, 3, 4, 5], 
    [ 6, 7, 8, 9,10], 
    [11,12,13,14,15],
    [16,17,18,19,20],
    [21,22,23,24,25],
]
a = [
    [1,2,3], 
    [4,5,6], 
    [7,8,9]
]

res = rotateImage(a)
print(res)
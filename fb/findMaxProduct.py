from heapq import heapify, heappush, heappop

def findMaxProduct(arr):
    h = []
    heapify(h)
    sol = []
    for x in arr:
        heappush(h, -x)
        if len(h) < 3:
            sol.append(-1)            
            continue

        v1 = -heappop(h)
        v2 = -heappop(h)
        v3 = -heappop(h)
        sol.append( v1 * v2 * v3 )
        heappush(h, -v1)
        heappush(h, -v2)
        heappush(h, -v3)
    return sol


def test_code() -> None:
    # Test 1)
    arr = [ 1, 2, 3, 4, 5 ]
    assert findMaxProduct(arr)
    print("success")

if __name__ == "__main__":
    test_code()

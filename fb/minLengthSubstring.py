from collections import Counter

def minLengthSubstring(s, t):
    size = len(s)
    b_map = Counter()
    s_map = Counter()
    for b in s:
        b_map[b] += 1
    for c in t:
        s_map[c] += 1

    min_size = float('inf')
    for i in range(size):
        copy = s_map.copy()
        j = i
        while j < size:
            cur = s[j]
            if cur in copy:
                copy[cur] -= 1
                if copy[cur] == 0:
                    del copy[cur]
                    if len(copy) == 0:
                        min_size = min(min_size, j - i + 1)
                        break
            j += 1
        i += 1

    if min_size == float('inf'):
        return -1
    return min_size



def test_code() -> None:
    assert minLengthSubstring(
        "dcbefebce",
        "fd"
    ) == 5

    assert minLengthSubstring(
        "bfbeadbcbcbfeaaeefcddcccbbbfaaafdbebedddf",
        "cbccfafebccdccebdd"
    ) == -1
    print("success")

if __name__ == "__main__":
    test_code()

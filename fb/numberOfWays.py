from collections import Counter
def numberOfWays(arr, k):
    mapped = Counter()
    for c in arr:
        mapped[c] += 1

    count = 0
    for c in set(arr):
        diff = k - c
        if diff not in mapped:
            continue

        if diff == c:
            n = mapped[diff] - 1
            add = int(n*(n+1) / 2)
        else:
            add = mapped[diff]
        del mapped[c]
        count += add

    return count

# aa=1
# aaa=21
# abcd=321=6
# abcde=4321

res = numberOfWays([1, 2, 3, 4, 3], 6)
print(res)

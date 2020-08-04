from typing import List
from functools import cmp_to_key


weirdList = [
    {
        "a": 1,
        "b": 3,
    },
    {
        "a": 1,
        "b": 2,
    },
    {
        "a": 2,
        "b": 1,
    },
]
def owncomp(a, b):
    if a["a"] > b["a"]:
        return 1
    elif a["a"] < b["a"]:
        return -1
    
    if a["b"] > b["b"]:
        return 1
    else:
        return -1

rs = sorted(weirdList, key=cmp_to_key(owncomp))
print(rs)

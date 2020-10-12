import time
start_time = time.time()

memo = {}
def fbrec(target, words):
    if target == "":
        return [[]]
    
    if target in memo:
        return memo[target]

    results = []
    for i in range(0 ,len(target)):
        first = target[0:i+1]
        sec = target[i+1:]
        if first in words:
            res = fbrec(sec, words)
            if res:
                for item in res:
                    results.append([first] + item)

    memo[target] = results
    return results

def fb(target, words):
    return fbrec(target, words)

res = fb(
    "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
    {
        "a": True,
        "aaaaaa": True,
    }
)
print("--- %s seconds ---" % (time.time() - start_time))
# print(res)



# def fbrec(target, words):
#     if target == "":
#         return True
#     for i in range(0 ,len(target)):
#         first = target[0:i+1]
#         sec = target[i+1:]
#         if first in words:
#             res = fb(sec, words)
#             if res:
#                 return True

#     return False
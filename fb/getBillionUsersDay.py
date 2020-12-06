# https://www.facebookrecruiting.com/portal/coding_practice_question/?problem_id=951929261870357

def getBillionUsersDay(head):
    pass

# TODO

res = getBillionUsersDay([1.1, 1.2, 1.3]) # 79
# res = getBillionUsersDay([1.01, 1.02]) # 1047
print(res)



























# def sumDay(arr, t):
#   running = 0
#   for g in arr:
#     running += (g ** t)
#   return running

# def search(arr, low, high):
#   while low < high:
#     mid = low + (high - low) // 2
#     if sumDay(arr, mid) < 1000000000:
#       low = mid + 1
#     else:
#       high = mid
#   return high

# def getBillionUsersDay(growthRates):
#   i = 1
#   users = sumDay(growthRates, i)
#   if users >= 1000000000:
#     return 1

# # find the upper boundry
# while users < 1000000000:
#   i *= 2
#   users = sumDay(growthRates, i)

# # find the exact boundry
# return search(growthRates, i // 2, i)
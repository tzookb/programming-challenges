from functools import reduce

5000
def gcd(a, b):
    while b != 0:
        a, b = b , a % b
    return a
    if b == 0:
        return a
    return gcd(b, a%b)

def generalizedGCD(num, arr):
    def red(x, y):
        return gcd(x, y)
    product = reduce(red, arr)
    print(product)

# generalizedGCD(1, [
#     6,12,15,21
# ])

print(gcd(10, 20))
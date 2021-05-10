class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        sol = []
        for i in range(1,n+1):
            fizzbuzz = []
            if i % 3 == 0:
                fizzbuzz.append("Fizz")
            if i % 5 == 0:
                fizzbuzz.append("Buzz")

            if fizzbuzz:
                res = "".join(fizzbuzz)
            else:
                res = str(i)
            sol.append(res)
        return sol
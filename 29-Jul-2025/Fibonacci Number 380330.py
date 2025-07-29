# Problem: Fibonacci Number - https://leetcode.com/problems/fibonacci-number/

class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1

        f1, f2 = 0, 1
        for i in range(2, n + 1):
            fn = f1 + f2
            f1, f2 = f2, fn
        return fn
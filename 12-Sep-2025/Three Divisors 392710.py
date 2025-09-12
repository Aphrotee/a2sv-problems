# Problem: Three Divisors - https://leetcode.com/problems/three-divisors/description/?envType=problem-list-v2&envId=number-theory

class Solution:
    def isThree(self, n: int) -> bool:
        count = 0

        for d in range(1, n + 1):
            if n % d == 0:
                count += 1
            if count > 3:
                return False
        return count == 3
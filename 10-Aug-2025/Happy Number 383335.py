# Problem: Happy Number - https://leetcode.com/problems/happy-number/description/

class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1 and (n not in seen):
            seen.add(n)
            total_sum = 0
            while n > 0:
                total_sum += ((n % 10) ** 2)
                n //= 10

            n = total_sum

        return n == 1

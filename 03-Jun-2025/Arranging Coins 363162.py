# Problem: Arranging Coins - https://leetcode.com/problems/arranging-coins/description/

class Solution:
    def arrangeCoins(self, n: int) -> int:
        a = 1
        b = 1
        c = -2 * n
        if n == 1:
            return 1

        x = (-b - math.sqrt((b ** 2) - (4 * a * c))) / (2 * a)
        y = (-b + math.sqrt((b ** 2) - (4 * a * c))) / (2 * a)
        return int(max(x, y))

        
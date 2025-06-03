# Problem: Arranging Coins - https://leetcode.com/problems/arranging-coins/description/

class Solution:
    def arrangeCoins(self, n: int) -> int:
        rows = 0
        need = 1
        while n >= need:
            rows += 1
            n -= need
            need += 1
        return rows

        
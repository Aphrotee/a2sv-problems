# Problem: Last Stone Weight II - https://leetcode.com/problems/last-stone-weight-ii/description/

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        self.answer = float("inf")
        self.n = len(stones)
        self.memo = {}

        def dp(index, total):
            if index == self.n:
                if total >= 0:
                    self.answer = min(self.answer, total)
                return self.answer
            if (index, total) in self.memo:
                return self.memo[(index, total)]
            
            self.memo[(index, total)] = min(dp(index + 1, total + stones[index]),
                    dp(index + 1, total - stones[index]))
            return self.memo[(index, total)]
        
        return dp(0, 0)
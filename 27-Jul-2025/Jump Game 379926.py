# Problem: Jump Game - https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        extreme = 0
        n = len(nums)

        for i, num in enumerate(nums):
            if i > extreme:
                return False
            farthest = i + num
            extreme = max(extreme, farthest)
            if extreme >= n - 1:
                return True
        return False
# Problem: Jump Game - https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        far = 0
        n = len(nums)
        for pos in range(n):
            if pos == n-1:
                return True
            far = max(nums[pos] + pos, far)
            if pos >= far:
                return False
        return True

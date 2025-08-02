# Problem: Jump Game II - https://leetcode.com/problems/jump-game-ii/description/

class Solution:
    def jump(self, nums: List[int]) -> int:
        maxReached = 0
        count = 0
        endpoint = 0
        n = len(nums)
        i = 0
        while i < n:
            newPosition = i + nums[i]
            if i == n - 1:
                break

            maxReached = max(newPosition, maxReached)
            if i == endpoint:
                endpoint = maxReached
                count += 1
            i += 1
        return count

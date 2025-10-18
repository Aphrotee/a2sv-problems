# Problem: Jump Game II - https://leetcode.com/problems/jump-game-ii/description/

class Solution:
    def jump(self, nums: List[int]) -> int:
        far = 0
        curr_far = 0
        jumps = 0
        n = len(nums)

        for pos in range(n):
            if curr_far >= n - 1:
                return jumps
            far = max(far, nums[pos] + pos)  
            if pos == curr_far:
                if far > curr_far:
                    curr_far = far
                    jumps += 1
# [4,1,5,5,4,5,2,1,2]
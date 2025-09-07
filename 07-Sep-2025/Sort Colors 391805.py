# Problem: Sort Colors - https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        l, r = 0, n - 1
        curr = 0
        while curr <= r:
            
            if nums[curr] == 0:
                nums[curr], nums[l] = nums[l], nums[curr]
                l += 1
                if nums[curr] == 0:
                    curr += 1
            elif nums[curr] == 2:    
                nums[curr], nums[r] = nums[r], nums[curr]
                r -= 1
                # curr += 1
            else:
                curr += 1
        
        # 2,0,1 l: 0, r: 2, c: 0
        # 1,0,2 l: 0, r: 1, c: 1
        # 1,0,2 l: 0, r: 1, c: 1
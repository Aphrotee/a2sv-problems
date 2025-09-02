# Problem: Sort an Array - https://leetcode.com/problems/sort-an-array/description/

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 1:
            return nums

        m = n // 2
        left_side = nums[:m]
        right_side = nums[m:]

        return self.merge(self.sortArray(left_side), self.sortArray(right_side))
            
    
    
    def merge(self, left: List[int], right: List[int]) -> List[int]:
        l = len(left)
        r = len(right)

        i, j = 0, 0

        ans = []
        while i < l or j < r:
            if i < l and j < r:
                if left[i] <= right[j]:
                    ans.append(left[i])
                    i += 1
                elif right[j] < left[i]:
                    ans.append(right[j])
                    j += 1
            elif i < l:
                ans.append(left[i])
                i += 1
            elif j < r:
                ans.append(right[j])
                j += 1
        return ans
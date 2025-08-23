# Problem: 3Sum - https://leetcode.com/problems/3sum/description/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        n = len(nums)
        nums.sort()

        for k in range(n - 1):
            l = k + 1
            r = n - 1
            target = -nums[k]
            while l < r:
                if nums[r] + nums[l] == target:
                    potential = (nums[k], nums[l], nums[r])
                    if potential not in ans:
                        ans.add(potential)
                    l += 1
                elif nums[r] + nums[l] > target:
                    r -= 1
                elif nums[r] + nums[l] < target:
                    l += 1
                else:
                    l += 1
        return [list(a) for a in ans]


# Problem: Permutations - https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        n = len(nums)

        def perm(index):
            nonlocal n, ans
            if index == n:
                return
            temp = []

            for ordering in ans:
                for pos in range(0, len(ordering) + 1):
                    temp.append(ordering[:pos] + [nums[index]] + ordering[pos:])
            ans = temp
            perm(index + 1)
        perm(0)
        return ans

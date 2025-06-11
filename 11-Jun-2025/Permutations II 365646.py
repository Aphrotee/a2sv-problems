# Problem: Permutations II - https://leetcode.com/problems/permutations-ii/description/

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.permutations = set()
        n = len(nums)

        def permute(perm, index):
            if index == n:
                self.permutations.add(tuple(perm))
                return
            for i in range(len(perm) + 1):
                temp = perm[:]
                temp.insert(i, nums[index])
                permute(temp, index + 1)
        permute([], 0)

        answer = []

        for permutation in self.permutations:
            answer.append(list(permutation))
        return answer
            
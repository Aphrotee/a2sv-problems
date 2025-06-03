# Problem: Combinations - https://leetcode.com/problems/combinations/

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        answer = []

        def dfs(current, count, comb):
            nonlocal answer
            if count == k:
                answer.append(comb)
                return
            if current > n:
                return
            dfs(current + 1, count + 1, comb + [current])
            dfs(current + 1, count, comb)
            
        dfs(1, 0, [])
        return answer
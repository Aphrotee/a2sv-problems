# Problem: Solving Questions with Brainpower - https://leetcode.com/problems/solving-questions-with-brainpower/

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = {}

        def dfs(index):
            # print(index, point)
            if index >= n:
                return 0
            
            if index in dp:
                return dp[index]
            
            dp[index] = max(dfs(index + 1),
                            dfs(index + questions[index][1] + 1) + questions[index][0])
            
            return dp[index] 
        return dfs(0)
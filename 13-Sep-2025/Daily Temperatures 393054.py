# Problem: Daily Temperatures - https://leetcode.com/problems/daily-temperatures/

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        stack = []
        
        for i, temp in enumerate(temperatures):
            while stack and stack[-1][-1] < temp:
                index, lowerTemp = stack.pop()
                ans[index] = (i - index)
            stack.append([i, temp])
        return ans
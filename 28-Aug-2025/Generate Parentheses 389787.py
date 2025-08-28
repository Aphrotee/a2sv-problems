# Problem: Generate Parentheses - https://leetcode.com/problems/generate-parentheses/description/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.ans = []

        def dfs(parenthesis, balance, count):
            if count > n:
                return
            elif count == n:
                if balance == 0:
                    self.ans.append(''.join(parenthesis))
                    return
                elif balance < 0:
                    return
            
            if count < n:
                parenthesis.append("(")
                dfs(parenthesis, balance + 1, count + 1)
                parenthesis.pop()
            if balance > 0:
                parenthesis.append(")")
                dfs(parenthesis, balance - 1, count)
                parenthesis.pop()
        
        dfs([], 0, 0)
        return self.ans
# Problem: Generate Parentheses - https://leetcode.com/problems/generate-parentheses/description/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = set()

        # for _ in range(n - 1):
        #     temp = set()
        #     for parenth in answer:
        #         n = len(parenth)
        #         for i in range(n + 1):
        #             newParenth = parenth[:i] + "()" + parenth[i:]
        #             temp.add(newParenth)
        #     answer = temp

        def dfs(paren, counter, size):
            if size == n * 2:
                if counter == 0:
                    answer.add(''.join(paren))
                return
            if counter < 0:
                return
            
            paren.append('(')
            dfs(paren, counter + 1, size + 1)
            paren.pop()
            paren.append(')')
            dfs(paren, counter - 1, size + 1)
            paren.pop()
        dfs([], 0, 0)
        return list(answer)
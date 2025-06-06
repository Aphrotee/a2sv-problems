# Problem: Generate Parentheses - https://leetcode.com/problems/generate-parentheses/description/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = set(["()"])

        for _ in range(n - 1):
            temp = set()
            for parenth in answer:
                n = len(parenth)
                for i in range(n + 1):
                    newParenth = parenth[:i] + "()" + parenth[i:]
                    temp.add(newParenth)
            answer = temp
        return list(answer)
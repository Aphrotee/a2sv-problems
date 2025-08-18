# Problem: Evaluate Reverse Polish Notation - https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        op = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: x / y,
        }
        for t in tokens:
            if t in "+/-*" and stack:
                stack[-2] = int(op[t](stack[-2], stack[-1]))
                stack.pop()
            else:
                stack.append(int(t))
        return stack[0]
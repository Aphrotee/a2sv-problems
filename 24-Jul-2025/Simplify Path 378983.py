# Problem: Simplify Path - https://leetcode.com/problems/simplify-path/

class Solution:
    def simplifyPath(self, path: str) -> str:
        directories = path.split("/")
        stack = []
        for directory in directories:
            if directory:
                if directory == "..":
                    if stack:
                        stack.pop()
                elif directory == '.':
                    continue
                else:
                    stack.append(directory)
        return "/" + '/'.join(stack)
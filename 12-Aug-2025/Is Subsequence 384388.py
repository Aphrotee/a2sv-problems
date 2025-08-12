# Problem: Is Subsequence - https://leetcode.com/problems/is-subsequence/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        index = 0
        if len(s) > len(t):
            return False
        ns = len(s)

        for char in t:
            if index == ns:
                return True
            if char == s[index]:
                index += 1
        return index == ns
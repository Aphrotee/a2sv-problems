# Problem: Palindrome Partitioning - https://leetcode.com/problems/palindrome-partitioning/

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        ans = []
        def get_palindromes(start, current):
            nonlocal n, ans
            if start == n:
                return
            
            for nextEnd in range(start + 1, n + 1):
                if self.is_palindrome(s, start, nextEnd  - 1):
                    current.append(s[start:nextEnd])
                    if nextEnd == n:
                        ans.append(current[:])
                    else:
                        get_palindromes(nextEnd, current)
                    current.pop()
        get_palindromes(0, [])
        return ans
    
    def is_palindrome(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
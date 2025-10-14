# Problem: Palindromic Substrings - https://leetcode.com/problems/palindromic-substrings/description/

class Solution:
    def countSubstrings(self, s: str) -> int:
        palindromes = 0
        def getLongestPalindrome(l, r):
            nonlocal palindromes
            while l >=0 and r < len(s) and s[l] == s[r]:
                palindromes += 1
                l -= 1
                r += 1
            return

        for i in range(len(s)):
            getLongestPalindrome(i, i)
            getLongestPalindrome(i, i + 1)
            
        return palindromes
        
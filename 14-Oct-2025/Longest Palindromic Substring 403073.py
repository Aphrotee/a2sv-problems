# Problem: Longest Palindromic Substring - https://leetcode.com/problems/longest-palindromic-substring/description/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def getLongestPalindrome(l, r):
            while l >=0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1:r]

        longestPalindrome = ""
        for i in range(len(s)):
            palindrome1 = getLongestPalindrome(i, i)
            palindrome2 = getLongestPalindrome(i, i + 1)
            if len(palindrome1) > len(longestPalindrome):
                longestPalindrome = palindrome1
            if len(palindrome2) > len(longestPalindrome):
                longestPalindrome = palindrome2
        return longestPalindrome
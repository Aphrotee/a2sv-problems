# Problem: Longest Palindromic Substring - https://leetcode.com/problems/longest-palindromic-substring/description/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        longest = ''

        def getPalindrome(l: int, r: int, single: bool):
            left = []
            right = []
            while l >= 0 and r < n and s[l] == s[r]:
                left.append(s[l])
                right.append(s[r])
                l -= 1
                r += 1
            left.reverse()
            if single:
                if left:
                    left.pop()
            
            return ''.join(left + right)

        for i in range(n):
            leftPalindrome = getPalindrome(i, i, True)
            rightPalindrome = getPalindrome(i, i + 1, False)
            if len(leftPalindrome) > len(longest):
                longest = leftPalindrome
            if len(rightPalindrome) > len(longest):
                longest = rightPalindrome
        return longest
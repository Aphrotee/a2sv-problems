# Problem: Minimum Window Substring - https://leetcode.com/problems/minimum-window-substring/submissions/

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        m = len(t)

        count_t = [0] * 52
        count_s = [0] * 52

        for c in t:
            if c.islower():
                count_t[ord(c) - ord('a')] += 1
            else:
                count_t[26 + ord(c) - ord('A')] += 1
        minLength = float("inf")
        l, r = -1, -1
        left = 0

        for right in range(n):
            rightChar = s[right]
            if rightChar.islower():
                count_s[ord(rightChar) - ord('a')] += 1
            else:
                count_s[26 + ord(rightChar) - ord('A')] += 1
            while left <= right and self.check_substring(count_s, count_t):
                if right - left + 1 < minLength:
                    l, r = left, right
                    minLength = right - left + 1
                leftChar = s[left]
                if leftChar.islower():
                    count_s[ord(leftChar) - ord('a')] -= 1
                else:
                    count_s[26 + ord(leftChar) - ord('A')] -= 1      
                left += 1          

        return s[l:r + 1]



    def check_substring(self, sCount, tCount):
        for i in range(52):
            if sCount[i] < tCount[i]:
                return False
        return True
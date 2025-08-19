# Problem: Valid Anagram - https://leetcode.com/problems/valid-anagram/description/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sc = [0] * 26
        tc = [0] * 26

        for c in s:
            sc[ord(c) - ord('a')] += 1
        
        for c in t:
            tc[ord(c) - ord('a')] += 1
        return tc == sc
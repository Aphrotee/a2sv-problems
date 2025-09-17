# Problem: Permutation in String - https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = [0] * 26
        m = len(s1)

        for ch in s1:
            count1[ord(ch) - ord('a')] += 1
        
        windowCount = [0] * 26
        n = len(s2)
        l = 0
        for r in range(n):
            windowCount[ord(s2[r]) - ord('a')] += 1
            if r - l + 1 == m:
                if count1 == windowCount:
                    return True
                windowCount[ord(s2[l]) - ord('a')] -= 1
                l += 1
        return False
                
        
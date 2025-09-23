# Problem: Check if All Characters Have Equal Number of Occurrences - https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/description/

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        count = {}
        for c in s:
            count[c] = 1 + count.get(c, 0)
        return len(set(count.values())) == 1
# Problem: longest-substring-without-repeating-characters - https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        n = len(s)
        store = defaultdict(int)
        max_len = 0

        if n <= 1:
            return n

        for r in range(n):
            store[s[r]] += 1
            max_len = max(max_len, r - l)
            while store[s[r]] > 1:
                store[s[l]] -= 1
                l += 1
        return max(max_len, r - l + 1)
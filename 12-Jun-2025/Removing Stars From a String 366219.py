# Problem: Removing Stars From a String - https://leetcode.com/problems/removing-stars-from-a-string/description/

class Solution:
    def removeStars(self, s: str) -> str:
        nonStar = []
        for char in s:
            if char != "*":
                nonStar.append(char)
            else:
                nonStar.pop()
        return ''.join(nonStar)
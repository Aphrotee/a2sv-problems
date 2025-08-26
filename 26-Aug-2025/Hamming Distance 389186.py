# Problem: Hamming Distance - https://leetcode.com/problems/hamming-distance/

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        dist = x ^ y

        ans = 0

        while dist:
            ans += (dist % 2)
            dist //= 2
        return ans
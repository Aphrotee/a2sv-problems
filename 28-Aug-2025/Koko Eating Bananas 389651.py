# Problem: Koko Eating Bananas - https://leetcode.com/problems/koko-eating-bananas/

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)

        def can_finish(piles, kk):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / kk)
            return hours

        l = 1
        r = max(piles)
        time = r

        while l < r:
            m = l + ((r - l) // 2)
            if can_finish(piles, m) <= h:
                time = min(time, m)
                r = m
            else:
                l = m + 1
        return time
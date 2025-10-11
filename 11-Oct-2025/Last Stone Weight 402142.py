# Problem: Last Stone Weight - https://leetcode.com/problems/last-stone-weight/

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stone_heap = []
        for stone in stones:
            heappush(stone_heap, -stone)

        while len(stone_heap) > 1:
            y = -heappop(stone_heap)
            x = -heappop(stone_heap)
            if x < y:
                heappush(stone_heap, x - y)
        return -heappop(stone_heap) if len(stone_heap) else 0

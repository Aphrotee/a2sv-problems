# Problem: Rabbits in Forest - https://leetcode.com/problems/rabbits-in-forest/

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = {}

        for c in answers:
            count[c] = 1 + count.get(c, 0)

        rabbits = 0
        for c, freq in count.items():
            rabbits += (math.ceil(freq / (c + 1)) * (c + 1))
        return rabbits
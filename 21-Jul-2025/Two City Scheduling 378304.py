# Problem: Two City Scheduling - https://leetcode.com/problems/two-city-scheduling/

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        diffs = []
        for a, b in costs:
            diffs.append((a, b, a-b))
        diffs.sort(key=lambda x: x[-1])

        cost = 0
        n = len(costs)
        # print(costs, costsB)

        k = 1
        for a, b, d in diffs:
            if k <= n // 2:
                cost += a
            else:
                cost += b
            k += 1
        return cost
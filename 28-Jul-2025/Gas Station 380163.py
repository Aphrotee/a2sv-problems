# Problem: Gas Station - https://leetcode.com/problems/gas-station/

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        size = len(cost)
        sumDiff = 0
        maxDiff = 0
        start = 0

        for i in range(size - 1, -1, -1):
            # get the differences of all the cost and gas at each gas station
            newDiff = gas[i] - cost[i]
            sumDiff += newDiff
            # use the difference build a cummulative sum backwards
            if sumDiff > maxDiff:
                # the point where the cummulative sum of the
                # differences is maximum is the suitable start point
                start = i
                maxDiff = sumDiff

        if sumDiff < 0:
            # if the cummulative sum is less than 0,
            # it is impossible to go round te gas station starting from any point
            return -1

        return start
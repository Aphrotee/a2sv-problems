# Problem: Merge Intervals (Optional) - https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        output = [intervals[0]]
        n = len(intervals)
        for i in range(1, n):
            if output[-1][-1] >= intervals[i][0]:
                output[-1][-1] = max(output[-1][-1], intervals[i][-1])
                # output[-1][0] = min(output[-1][0], intervals[i][0])
            else:
                output.append(intervals[i])
        return output
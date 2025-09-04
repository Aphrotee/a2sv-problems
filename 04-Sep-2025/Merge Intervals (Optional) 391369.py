# Problem: Merge Intervals (Optional) - https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        n = len(intervals)
        ans = [intervals[0]]

        for i in range(1, n):
            if ans[-1][1] < intervals[i][0]:
                ans.append(intervals[i])
            else:
                start = min(ans[-1][0], intervals[i][0])
                end = max(ans[-1][1], intervals[i][1])
                ans[-1][0] = start
                ans[-1][1] = end
        return ans
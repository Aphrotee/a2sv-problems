# Problem: Find Right Interval - https://leetcode.com/problems/find-right-interval/

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        indexed_intervals = [[intervals[i][0], intervals[i][1], i] for i in range(n)]
        ans = [-1] * n
        indexed_intervals.sort()
        def get_right(lower, l, r):
            nonlocal n
            res = -1
            while l < r:
                m = l + ((r - l) // 2)
                if indexed_intervals[m][0] == lower:
                    res = indexed_intervals[m][2]
                    return res
                elif indexed_intervals[m][0] > lower:
                    res = indexed_intervals[m][2]
                    r = m
                elif indexed_intervals[m][0] < lower:
                    l  = m + 1
            if l < n and indexed_intervals[l][0] >= lower:
                return indexed_intervals[l][2]
            return res


        for i in range(n):
            start, end, index = indexed_intervals[i]
            ans[index] = get_right(end, i, n - 1)
        
        return ans

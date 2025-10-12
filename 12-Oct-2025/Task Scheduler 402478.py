# Problem: Task Scheduler - https://leetcode.com/problems/task-scheduler/

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {}

        for task in tasks:
            count[task] = 1 + count.get(task, 0)
        
        time = 0
        heap = []
        for task, freq in count.items():
            heappush(heap, [0, freq])
        
        while heap:
            minTime, freq = heappop(heap)
            if minTime <= time:
                if freq - 1 > 0:
                    heappush(heap, [minTime + n + 1, freq - 1])
                time += 1
            else:
                heappush(heap, [minTime, freq])
                time = minTime
        return time
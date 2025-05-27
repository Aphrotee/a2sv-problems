# Problem: Task Scheduler - https://leetcode.com/problems/task-scheduler/

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}

        for task in tasks:
            freq[task] = 1 + freq.get(task, 0)
        
        queue = [[0, task] for task in freq]
        time = 0
        while queue:
            nextTask = heapq.heappop(queue)
            if nextTask[0] <= time:
                freq[nextTask[1]] -= 1
                nextTask[0] += n + 1
            if freq[nextTask[1]] > 0:
                heapq.heappush(queue, nextTask)
            time += 1
        return time

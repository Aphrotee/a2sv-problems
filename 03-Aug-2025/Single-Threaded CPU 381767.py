# Problem: Single-Threaded CPU - https://leetcode.com/problems/single-threaded-cpu/

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        for i, task in enumerate(tasks):
            enqueue, process = task
            tasks[i] = [enqueue, process, i]
        
        tasks.sort()
        time = tasks[0][0]
        end = -1
        ans = []

        processIndex = 0
        heap = []

        while len(ans) < n: 
            while processIndex < n and tasks[processIndex][0] <= time:
                heapq.heappush(heap, [tasks[processIndex][1], tasks[processIndex][2]])
                processIndex += 1
            if heap:
                size, index = heapq.heappop(heap)
                time += size
                ans.append(index)
            else:
                time = tasks[processIndex][0]

        return ans
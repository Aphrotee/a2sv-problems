# Problem: Single-Threaded CPU - https://leetcode.com/problems/single-threaded-cpu/

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        for i, task in enumerate(tasks):
            tasks[i] = [task[0], task[1], i]
        tasks.sort(key=lambda x: x[0])
        
        heap = []
        end = 0
        time = tasks[0][0]
        ans = []
        to_add = 0
        while len(ans) < n:
            while to_add < n and tasks[to_add][0] <= time:
                heapq.heappush(heap, [tasks[to_add][1], tasks[to_add][2]])
                to_add += 1
            if heap:
                current = heapq.heappop(heap)
                size, index = current
                ans.append(index)
                end = time + size
                time = end
            else:
                time = tasks[to_add][0]
        return ans
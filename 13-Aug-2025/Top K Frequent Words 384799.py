# Problem: Top K Frequent Words - https://leetcode.com/problems/top-k-frequent-words/

class HeapItem:

    def __init__(self, word, count):
        self.word = word
        self.count = count

    def __lt__(self, compare):
        if self.count == compare.count:
            return self.word > compare.word
        else:
            return self.count < compare.count

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        store = {}
        n = len(words)

        for word in words:
            store[word] = 1 + store.get(word, 0)
        
        heap = []

        for word, count in store.items():
            heapq.heappush(heap, HeapItem(word, count))
            if len(heap) > k:
                heapq.heappop(heap)
        ans = []
        buckets = [[] for _ in range(n + 1)]
        while heap:
            item = heapq.heappop(heap)
            ans.append(item.word)
        ans.reverse()
        return ans

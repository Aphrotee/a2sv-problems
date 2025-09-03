# Problem: Find K Pairs with Smallest Sums - https://leetcode.com/problems/find-k-pairs-with-smallest-sums/description/

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        i, j = 0, 0
        n, m = len(nums1), len(nums2)

        heap = []
        anss = []
        seen = set([0, 0])

        heapq.heappush(heap, (nums1[i] + nums2[j], i, j))

        while k > 0 and heap:
            s, i, j = heapq.heappop(heap)
            anss.append([nums1[i], nums2[j]])
            if i + 1 < n and (i + 1, j) not in seen:
                heapq.heappush(heap, [nums1[i + 1] + nums2[j], i + 1, j])
                seen.add((i + 1, j))

            if j + 1 < m and (i, j + 1) not in seen:
                heapq.heappush(heap, [nums1[i] + nums2[j + 1], i, j + 1])
                seen.add((i, j + 1))
            k -= 1

        return anss
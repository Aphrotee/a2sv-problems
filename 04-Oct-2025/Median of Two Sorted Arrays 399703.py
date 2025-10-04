# Problem: Median of Two Sorted Arrays - https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) <= len(nums2):
            return self.findMedian(nums1, nums2)
        else:
            return self.findMedian(nums2, nums1)
        
    
    def findMedian(self, numsA, numsB):
        m = len(numsA)
        n = len(numsB)
        size = m + n
        half = size // 2

        l, r = 0, m - 1
        while True:
            i = (l + r) // 2
            j = half - i - 2

            leftA = numsA[i] if i >= 0 else float("-inf")
            rightA = numsA[i + 1] if (i + 1) < m else float("inf")
            leftB = numsB[j] if j >= 0 else float("-inf")
            rightB = numsB[j + 1] if (j + 1) < n else float("inf")

            if leftA <= rightB and leftB <= rightA:
                if size % 2 == 0:
                    return (max(leftA, leftB) + min(rightA, rightB)) / 2
                else:
                    return min(rightA, rightB)
            elif leftA > rightB:
                r = i - 1
            else:
                l = i + 1

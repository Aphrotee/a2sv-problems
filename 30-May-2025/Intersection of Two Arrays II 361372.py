# Problem: Intersection of Two Arrays II - https://leetcode.com/problems/intersection-of-two-arrays-ii/

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter1 = {}
        counter2 = {}
        answer = []
        intersect = {}
        
        for num in nums1:
            counter1[num] = 1 + counter1.get(num, 0)
        for num in nums2:
            counter2[num] = 1 + counter2.get(num, 0)
        
        for num in nums1:
            intersect[num] = min(counter1.get(num, 0), counter2.get(num, 0))
        
        for num, freq in intersect.items():
            for _ in range(freq):
                answer.append(num)
        return answer
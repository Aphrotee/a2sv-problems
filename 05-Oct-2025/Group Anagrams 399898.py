# Problem: Group Anagrams - https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store = defaultdict(list)

        for s in strs:
            store[self.getKey(s)].append(s)

        return list(store.values())
    
    def getKey(self, string):
        count = [0] * 26

        for char in string:
            count[ord(char) - ord('a')] += 1
        return tuple(count)
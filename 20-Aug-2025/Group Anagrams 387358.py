# Problem: Group Anagrams - https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store = defaultdict(list)

        for s in strs:
            key = list(s)
            store[''.join(sorted(key))].append(s)

        return list(store.values())
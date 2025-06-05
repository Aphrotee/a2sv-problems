# Problem: Lexicographically Smallest Equivalent String - https://leetcode.com/problems/lexicographically-smallest-equivalent-string/

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        hmap = {}

        for a, b in zip(s1, s2):
            if a not in hmap:
                hmap[a] = set([a, b])
            if a in hmap:
                hmap[a].add(b)
                if b not in hmap:
                    hmap[b] = hmap[a]
                else:
                    hmap[a] = hmap[a].union(hmap[b])
                    for char in hmap[a]:
                        hmap[char] = hmap[a]
                    hmap[b] = hmap[a]
        # print(hmap)
        answer = []
        for char in baseStr:
            if char not in hmap:
                hmap[char] = set(char)
            answer.append(min(hmap[char]))
        return ''.join(answer)
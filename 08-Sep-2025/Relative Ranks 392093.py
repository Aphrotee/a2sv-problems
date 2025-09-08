# Problem: Relative Ranks - https://leetcode.com/problems/relative-ranks/description/

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_scores = sorted(score)
        n = len(score)
        places = {s: n - i for i, s in enumerate(sorted_scores)}

        places[sorted_scores[-1]] = "Gold Medal"
        if n > 1:
            places[sorted_scores[-2]] = "Silver Medal"
        if n > 2:
            places[sorted_scores[-3]] = "Bronze Medal"

        
        ans = []
        
        for s in score:
            ans.append(str(places[s]))
        return ans
        
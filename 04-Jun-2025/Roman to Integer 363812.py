# Problem: Roman to Integer - https://leetcode.com/problems/roman-to-integer/?envType=problem-list-v2&envId=string

class Solution:
    def romanToInt(self, s: str) -> int:
        romanDict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        num = 0
        temp = romanDict[s[0]]
        n = len(s)
        for i in range(1, n):
            if romanDict[s[i]] > temp:
                num -= temp
            else:
                num += temp
            temp = romanDict[s[i]]
        num += temp
        return num

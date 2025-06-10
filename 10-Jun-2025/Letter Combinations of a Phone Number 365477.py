# Problem: Letter Combinations of a Phone Number - https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        n = len(digits)


        answer = []

        def combine(letters, index):
            if index == n:
                answer.append(''.join(letters[:]))
                return
            
            for char in phone[digits[index]]:
                letters.append(char)
                combine(letters, index + 1)
                letters.pop()
            
        if digits:
            combine([], 0)
        return answer
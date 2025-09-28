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
        ans = []
        n = len(digits)

        def combinations(index, current_letters):
            nonlocal ans, n
            if index == n:
                if current_letters:
                    ans.append("".join(current_letters))
                return
            
            chars = phone[digits[index]]
            for char in chars:
                current_letters.append(char)
                combinations(index + 1, current_letters)
                current_letters.pop()
            
        combinations(0, [])
        return ans
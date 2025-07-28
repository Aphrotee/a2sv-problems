# Problem: Lemonade Change
easy - https://leetcode.com/problems/lemonade-change/

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count = {5: 0, 10: 0, 20: 0}
        for bill in bills:
            count[bill] = 1 + count.get(bill, 0)
            change = bill - 5
            if change == 15:
                if count[10] and count[5]:
                    count[10] -= 1
                    count[5] -= 1
                elif count[5] >= 3:
                    count[5] -= 3
                else:
                    return False
            if change == 5:
                if count[5]:
                    count[5] -= 1
                else:
                    return False
        return True


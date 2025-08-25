# Problem: Number Complement - https://leetcode.com/problems/number-complement/

class Solution:
    def findComplement(self, num: int) -> int:
        binary = []
        while num > 0:
            digit = num % 2
            num //= 2
            binary.append(1 if digit == 0 else 0)
        ans = 0
        n = len(binary)
        for i in range(n):
            bit = binary[i]
            ans += (bit * (2 ** i))
        return ans
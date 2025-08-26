# Problem:  Add Binary - https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        ans = []
        n, m = len(a), len(b)
        l = max(m, n)
        carry = 0

        if a == "0" and b == "0":
            return "0"
        aa = a[::-1]
        bb = b[::-1]

        for i in range(l):
            x = y = 0
            if i < n:
                x = int(aa[i])
            if i < m:
                y = int(bb[i])
            temp = carry + x + y
            ans.append(str(temp % 2))
            carry = temp // 2
        if carry:
            ans.append(str(carry))
        sanitized = []
        an = len(ans)
        temp = []
        while ans and ans[-1] == "0":
            ans.pop()
        return ''.join(ans[::-1])
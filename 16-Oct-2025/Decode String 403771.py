# Problem: Decode String - https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        i = 0
        n = len(s)
        def decode():
            nonlocal i, n
            k = 1
            k_dec = 0
            output = []

            while True:

                while i < n and s[i].isdigit():
                    k_dec = (k_dec * 10) + int(s[i])
                    i += 1
                if k_dec > 0:
                    k = k_dec
                    k_dec = 0
                temp = []
                if i < n and s[i] == "[":
                    i += 1
                    temp = decode()
                else:
                    while i < n and s[i].isalpha():
                        temp.append(s[i])
                        i += 1
                output.append(''.join(temp) * k)
                k = 1

                if i >= n or s[i] == ']':
                    i += 1
                    return ''.join(output)
        return decode()

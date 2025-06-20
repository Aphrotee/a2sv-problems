# Problem: Restore IP Addresses - https://leetcode.com/problems/restore-ip-addresses/

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        if n > 12:
            return []
        answers = []
        
        def restore(ip, index, dots):
            if index == n:
                if dots == 3:
                    strIP = ''.join(ip)
                    if self.isValidIP(strIP):
                        answers.append(strIP)
                return
            ip.append(s[index])
            restore(ip, index + 1, dots)
            ip.pop()
            if ip and dots < 3:
                ip.append(".")
                restore(ip, index, dots + 1)
                ip.pop()
        restore([], 0, 0)
        return answers
            
        
    def isValidIP(self, ip):
        nums = ip.split(".")
        if len(nums) != 4:
            return False
        for num in nums:
            if num == "0":
                continue
            elif num == "" or num[0] == "0":
                return False
            elif not (0 <= int(num) <= 255):
                return False
        return True
        
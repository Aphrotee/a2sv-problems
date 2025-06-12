# Problem: Crawler Log Folder - https://leetcode.com/problems/crawler-log-folder/

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        curr = ["main"]

        for log in logs:
            if log == "../":
                if len(curr) > 1:
                    curr.pop()
            elif log == "./":
                continue
            else:
                curr.append(log)
        return len(curr) - 1
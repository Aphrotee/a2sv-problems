# Problem: Accounts Merge - https://leetcode.com/problems/accounts-merge/

class Solution:
    def __init__(self):
        self.graph = defaultdict(set)

    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        names = defaultdict(str)
        for account in accounts:
            n = len(account)
            names[account[1]] = account[0]
            for i in range(2, n):
                self.graph[account[i - 1]].add(account[i])
                self.graph[account[i]].add(account[i - 1])
            if n == 2:
                self.graph[account[1]].add(account[1])
        self.seen = {}
        connected = []
        def dfs(node):
            if node in self.seen: 
                return
            
            self.seen[node] = False
            
            for neigh in self.graph[node]:
                if neigh not in self.seen:
                    dfs(neigh)
                else:
                    continue
            
            self.component.add(node)
            self.seen[node] = True

        ans = []
        for node in self.graph:
            if node not in self.seen:
                self.component = set()
                dfs(node)
                name = ""
                coms = []
                for com in self.component:
                    if not name:
                        name = names[com]
                    coms.append(com)
                ans.append([name] + sorted(coms))
        return ans
# Problem: Alian Dictionary - https://www.geeksforgeeks.org/problems/alien-dictionary/1

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        self.adj = {c: set() for word in words for c in word}
        n = 0
        m = len(words)

        for i in range(1, m):
            w1, w2 = words[i - 1], words[i]
            minLength = min(len(words[i]), len(words[i - 1]))
            for j in range(minLength):
                if w1[j]!= w2[j]:
                    self.adj[w1[j]].add(w2[j])
                    break
            if w1[:minLength] == w2[:minLength] and len(w2) < len(w1):
                return ""
        
        self.seen = {}
        self.ans = []
        def hasCycle(node):
            if node in self.seen:
                return self.seen[node]
            self.seen[node] = False
            
            for neighbour in self.adj[node]:
                if neighbour not in self.seen:
                    if not hasCycle(neighbour):
                        return False
                else:
                    if self.seen[neighbour] == False:
                        return False
                    else:
                        continue
                
            self.seen[node] = True
            self.ans.append(node)
            return True

        for start in self.adj:
            if start not in self.seen:
                if not hasCycle(start):
                    return ""

        return ''.join(self.ans[::-1])
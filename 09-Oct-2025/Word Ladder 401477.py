# Problem: Word Ladder - https://leetcode.com/problems/word-ladder/

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        adj = defaultdict(list)
        n = len(wordList)
        m = len(beginWord)
        wordSet = set(wordList)
        i = -1
        while i < n:
            word = beginWord if i == -1 else wordList[i]
            i += 1
            wordArr = list(word)
            for j in range(m):
                initialChar = wordArr[j]
                for AsciiVal in range(26):
                    wordArr[j] = chr(AsciiVal + ord('a'))
                    potential = ''.join(wordArr)
                    if potential in wordSet and potential != word:
                        adj[word].append(potential)
                wordArr[j] = initialChar        
        # print(adj)
        queue = deque([(beginWord, 1)])
        visited = set()
        while queue:
            word, length = queue.popleft()
            if word == endWord:
                return length
            if word in visited:
                continue
            visited.add(word)
            for nextWord in adj[word]:
                if nextWord not in visited:
                    queue.append((nextWord, length + 1))
        return 0
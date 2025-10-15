# Problem: Design Add and Search Words Data Structure - https://leetcode.com/problems/design-add-and-search-words-data-structure/

class TrieNode:
    def __init__(self, char):
        self.char = char
        self.end = False
        self.children = {}
    
    def addWord(self, word, index):
        if index == len(word):
            return
        char = word[index]
        if char in self.children:
            node = self.children[char]
        else:
            node = TrieNode(char)
            self.children[char] = node
        node.addWord(word, index + 1)
        if index == len(word) - 1:
            node.end = True


class WordDictionary:

    def __init__(self):
        self.root = TrieNode("")

    def addWord(self, word: str) -> None:
        self.root.addWord(word, 0)
        

    def search(self, word: str) -> bool:
        self.curr = self.root
        self.ans = False

        def check(curr, i):
            if i == len(word):
                if curr.end:
                    self.ans = True
                    return True
                return False
            if word[i] == ".":
                for child in curr.children.values():
                    if check(child, i + 1):
                        return True
            else:                
                if word[i] not in curr.children:
                    return False
                else:
                    if not check(curr.children[word[i]], i + 1):
                        return False
        check(self.root, 0)
        return self.ans

                        

    def checkPrefix(self, word: str, idx: int, curr: TrieNode) -> bool:
        if idx < len(word):
            if word[idx] == ".":
                print(word, word[idx], curr.children)
                for child in curr.children:
                    if idx == len(word) - 1:
                        if not curr.children[child].children:
                            self.node = curr.children[child]
                            return True
                    elif self.checkPrefix(word, idx + 1, curr.children[child]):
                        return True
                return False
            else:
                if word[idx] in curr.children:
                    if self.checkPrefix(word, idx + 1, curr.children[word[idx]]):
                        return True
                    else:
                        return False
                else:
                    return False
        self.node = curr
        return True


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
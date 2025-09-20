# Problem: LRU Cache - https://leetcode.com/problems/lru-cache/

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.keys = {}
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cap = capacity
    
    def makeNodeRecent(self, node: Node):
        if node.next is not None:
            node.next.prev = node.prev
        if node.prev is not None:
            node.prev.next = node.next

        self.head.next.prev = node
        node.next = self.head.next
        self.head.next = node
        node.prev = self.head
        if len(self.keys) > self.cap:
            keyToDelete = self.tail.prev.key
            nodeToDelete = self.keys[keyToDelete]
            nodeToDelete.prev.next = self.tail
            self.tail.prev = nodeToDelete.prev
            del self.keys[keyToDelete]
            del nodeToDelete

    def get(self, key: int) -> int:
        if key not in self.keys:
            return -1
        node = self.keys[key]
        self.makeNodeRecent(node)
        return node.val   

    def put(self, key: int, value: int) -> None:
        if key not in self.keys:
            node = Node(key, value)
        else:
            node = self.keys[key]
            node.val = value
        self.keys[key] = node
        self.makeNodeRecent(node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
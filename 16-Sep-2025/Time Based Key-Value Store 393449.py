# Problem: Time Based Key-Value Store - https://leetcode.com/problems/time-based-key-value-store/

class TimeMap:

    def __init__(self):
        self.keys = defaultdict(list)
        self.values = defaultdict(str)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keys[key].append(timestamp)
        self.values[timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        time = -1
        n = len(self.keys[key])
        l, r = 0, n - 1
        while l < r:
            m = l + ((r - l) // 2)
            if self.keys[key][m] == timestamp:
                return self.values[timestamp]
            elif self.keys[key][m] > timestamp:
                r = m
            else:
                time = self.keys[key][m]
                l = m + 1
        if l == r and self.keys[key][l] <= timestamp:
            time = self.keys[key][l]
        return self.values[time]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
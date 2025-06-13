# Problem: Find Consecutive Integers from a Data Stream - https://leetcode.com/problems/find-consecutive-integers-from-a-data-stream/

class DataStream:

    def __init__(self, value: int, k: int):
        self.stream = []
        self.k = k
        self.val = value
        

    def consec(self, num: int) -> bool:
        if num == self.val:
            if self.stream and self.stream[-1] != self.val:
                self.stream = []
            self.stream.append(num)
            if len(self.stream) >= self.k:
                return True
        else:
            self.stream = [num]
        return False

        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)
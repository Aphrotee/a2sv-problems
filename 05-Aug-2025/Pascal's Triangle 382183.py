# Problem: Pascal's Triangle - https://leetcode.com/problems/pascals-triangle/description/

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        rows = [[1]]

        for i in range(1, numRows):
            nextRow = [1]
            for j in range(len(rows[-1]) - 1):
                nextRow.append(rows[-1][j] + rows[-1][j + 1])
            nextRow.append(1)
            rows.append(nextRow)
        return rows

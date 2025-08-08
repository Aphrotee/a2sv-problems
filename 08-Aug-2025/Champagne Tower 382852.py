# Problem: Champagne Tower - https://leetcode.com/problems/champagne-tower/

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        tower = [[0 for _ in range(row + 1)] for row in range(query_row + 1)]
        tower[0][0] = poured

        for row in range(query_row + 1):
            for glass in range(row + 1):
                if glass == 0:
                    tower[row][glass] += max(tower[row - 1][glass] - 1, 0) / 2
                elif glass == row:
                    tower[row][glass] += max(tower[row - 1][glass - 1] - 1, 0) / 2
                else:
                    tower[row][glass] += (max(tower[row - 1][glass - 1] - 1, 0) / 2) + (max(tower[row - 1][glass] - 1, 0) / 2)
                if (row, glass) == (query_row, query_glass):
                    return min(tower[query_row][query_glass], 1)


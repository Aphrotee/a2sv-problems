# Problem: Employee Importance - https://leetcode.com/problems/employee-importance/

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        tree = {}

        for employee in employees:
            Id = employee.id
            tree[Id] = employee
        answer = 0
        queue = [id]
        while queue:
            emp = queue.pop(0)
            imp = tree[emp].importance
            answer += imp
            for sub in tree[emp].subordinates:
                queue.append(sub)
        return answer
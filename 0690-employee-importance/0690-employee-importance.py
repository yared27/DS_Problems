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
        totalImportance=0
        id_index={val.id: i for i,val in enumerate(employees)}
        def dfs(employeeId):
            nonlocal totalImportance
            totalImportance+=employees[id_index[employeeId]].importance
            for j in employees[id_index[employeeId]].subordinates:
                            dfs(j)

        dfs(id)
        return totalImportance


                








        
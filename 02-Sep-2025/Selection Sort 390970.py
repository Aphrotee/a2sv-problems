# Problem: Selection Sort - https://practice.geeksforgeeks.org/problems/selection-sort/1

class Solution: 
    def selectionSort(self, arr):
        n = len(arr)
        
        for minPos in range(n - 1):
            minIndex = minPos
            for potential in range(minPos, n):
                if arr[potential] < arr[minIndex]:
                    minIndex = potential
            arr[minIndex], arr[minPos] = arr[minPos], arr[minIndex]
        return arr
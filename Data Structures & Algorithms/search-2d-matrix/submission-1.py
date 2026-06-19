class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        t, b = 0, ROWS-1
        row_to_search = -1
        while t <= b:
            m = (t + b) // 2
            if matrix[m][0] <= target <= matrix[m][-1]:
                row_to_search = m
                break
            elif target > matrix[m][-1]:
                t = m+1
            else:
                b = m-1
        
        if row_to_search == -1: 
            return False
        
        row = matrix[row_to_search]

        l, r = 0, COLS-1
        while l <= r:
            m = (r + l) // 2
            if row[m] == target:
                return True
            elif target < row[m]:
                r = m-1
            else:
                l = m+1
        
        return False
        



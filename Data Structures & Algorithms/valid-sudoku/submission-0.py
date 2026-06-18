class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col_sets = [set() for i in range(9)]
        sub_grid_sets = [[set() for i in range(3)] for j in range(3)]

        for r in range(9):
            row_set = set()
            for c in range(9):
                cur_val = board[r][c]
                if cur_val != ".":
                    if cur_val in col_sets[c]:
                        return False
                    if cur_val in row_set:
                        return False
                    if cur_val in sub_grid_sets[r//3][c//3]:
                        return False
                    
                    row_set.add(cur_val)
                    col_sets[c].add(cur_val)
                    sub_grid_sets[r//3][c//3].add(cur_val)
        
        return True
                    

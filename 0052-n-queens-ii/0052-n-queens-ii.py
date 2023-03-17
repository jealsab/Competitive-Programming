class Solution:
    def __init__(self):
        self.result = 0
        self.valid_queen_pos  = set()
    
    def totalNQueens(self, n: int) -> int:

        self.backtrack(1, n)
        
        return self.result

    def backtrack(self, row, n):
        
        #base case
        if row > n:
            if len(self.valid_queen_pos) == n:
                self.result += 1
            return 
        
        for col in range(1, n+1):
            #if current position is valid, choose that position (pick and move)
            if self.isValid((row, col), self.valid_queen_pos, n):

                self.valid_queen_pos.add((row, col))
                self.backtrack(row + 1, n)
                self.valid_queen_pos.remove((row, col))
        
    
    def isValid(self, pos, valid_queen_pos, n):
        
        row, col = pos

        row_index = row
        #check if postion is valid vertically
        while row_index > 0:
            if (row_index, col) in valid_queen_pos:
                return False

            row_index -= 1

        
        row_index = row  
        diag_col = col
        #check if position is valid right diagnolally
        while row_index > 0 and diag_col <= n:
            if (row_index, diag_col) in valid_queen_pos:
                return False

            row_index -= 1
            diag_col += 1


        row_index = row  
        diag_col = col
        #check if position is valid left diagnolally
        while row_index > 0 and diag_col > 0:
            if (row_index, diag_col) in valid_queen_pos:
                return False

            row_index -= 1
            diag_col -= 1
        
        #otherwise return true
        return True
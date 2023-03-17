class Solution:
    def __init__(self):
        self.result = 0
        self.vertical = set()
        self.neg_diag = set()
        self.pos_diag = set()
    
    def totalNQueens(self, n: int) -> int:

        self.backtrack(1, n)
        
        return self.result

    def backtrack(self, row, n):
        
        #base case
        if row > n:
            self.result += 1
            return 
        
        for col in range(1, n+1):
            #if current position is valid, choose that position (pick and move)
            if self.isValid((row, col)):
                self.vertical.add(col)
                self.pos_diag.add(row+col)
                self.neg_diag.add(row-col)
                
                self.backtrack(row + 1, n)
                
                self.vertical.remove(col)
                self.pos_diag.remove(row+col)
                self.neg_diag.remove(row-col)
        
    
    def isValid(self, pos):
        row, col = pos
        
        if col in self.vertical or (row + col) in self.pos_diag or (row-col) in self.neg_diag:
            return False
        
        return True
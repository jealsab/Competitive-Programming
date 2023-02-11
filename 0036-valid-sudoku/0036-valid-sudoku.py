from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols =  defaultdict(set)
        rows = defaultdict(set)
        thrSquare = defaultdict(set)

        size = 9

        for r in range(size):
            for c in range(size):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in thrSquare[(r // 3,c // 3)]):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                thrSquare[(r // 3,c // 3)].add(board[r][c])
        return True


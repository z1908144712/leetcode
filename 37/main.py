from collections import defaultdict
from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def could_place(d, row, col):
            return not (d in rows[row] or d in columns[col] or d in boxs[box_index(row, col)])
        
        def place_number(d, row, col):
            rows[row][d] += 1
            columns[col][d] += 1
            boxs[box_index(row, col)][d] += 1
            board[row][col] = str(d)
        
        def remove_number(d, row, col):
            del rows[row][d]
            del columns[col][d]
            del boxs[box_index(row, col)][d]
            board[row][col] = '.'

        def place_next_numbers(row, col):
            if row == N - 1 and col == N - 1:
                nonlocal sudoku_solved
                sudoku_solved = True
            else:
                if col == N - 1:
                    backtrace(row + 1, 0)
                else:
                    backtrace(row, col + 1)
        
        def backtrace(row = 0, col = 0):
            if board[row][col] == '.':
                for d in range(1,10):
                    if could_place(d, row, col):
                        place_number(d, row, col)
                        place_next_numbers(row, col)
                        if not sudoku_solved:
                            remove_number(d, row, col)
            else:
                place_next_numbers(row, col)
        
        n = 3
        N = n * n
        box_index = lambda row, col:(row // n) * n + col // n
        rows = [defaultdict(int) for i in range(N)]
        columns = [defaultdict(int) for i in range(N)]
        boxs = [defaultdict(int) for i in range(N)]
        for i in range(N):
            for j in range(N):
                if board[i][j] != '.':
                    d = int(board[i][j])
                    place_number(d, i, j)
        sudoku_solved = False
        backtrace()
        return

if __name__ == "__main__":
    s = Solution()
    data = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    s.solveSudoku(data)
    print(data)

class Solution:
    def isValidSudoku(self, board: [[str]]) -> bool:
        tmp = []
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    if not (board[i][j] in tmp):
                        tmp.append(board[i][j])
                    else:
                        return False
            tmp.clear()
        for i in range(9):
            for j in range(9):
                if board[j][i] != '.':
                    if not (board[j][i] in tmp):
                        tmp.append(board[j][i])
                    else:
                        return False
            tmp.clear()
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    for g in range(3):
                        #print(i*3+k, j*3+g)
                        if board[i*3+k][j*3+g] != '.':
                            if not (board[i*3+k][j*3+g] in tmp):
                                tmp.append(board[i*3+k][j*3+g])
                            else:
                                return False
                tmp.clear()
        return True

if __name__ == "__main__":
    s = Solution()
    print(s.isValidSudoku([
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]))
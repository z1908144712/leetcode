from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def queen(A, cur = 0):
            if cur == n:
                s = []
                for v in A:
                    s.append("."*v+"Q"+"."*(n - v - 1))
                ans.append(s)
                return
            for col in range(n):
                A[cur], flag = col, True
                for row in range(cur):
                    if A[row] == col or abs(col - A[row]) == cur - row:
                        flag = False
                        break
                if flag:
                    queen(A, cur + 1)
        ans = []
        queen([None]*n)
        return ans

if __name__ == "__main__":
    s = Solution()
    print(s.solveNQueens(8))
from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrace(candidates, target):
            for i in range(len(candidates)):
                if target == candidates[i]:
                    path.append(candidates[i])
                    t = path[:]
                    t.sort()
                    if not t in ans:
                        ans.append(t)
                    path.pop()
                elif target > candidates[i]:
                    path.append(candidates[i])
                    backtrace(candidates[:i]+candidates[i+1:], target - candidates[i])
            if len(path) > 0:
                path.pop()
        ans, path = [], []
        backtrace(candidates, target)
        return ans

if __name__ == "__main__":
    s = Solution()
    print(s.combinationSum2([2,5,2,1,2], 5))
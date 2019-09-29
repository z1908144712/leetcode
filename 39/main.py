from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrace(trace, target):
            for x in candidates:
                t = trace.copy()
                if target == x:
                    t.append(x)
                    t.sort()
                    if not t in ans:
                        ans.append(t)
                elif target > x:
                    t.append(x)
                    backtrace(t, target - x)
        ans = []
        backtrace([], target)
        return ans

if __name__ == "__main__":
    s = Solution()
    print(s.combinationSum([2,3,5], 8))
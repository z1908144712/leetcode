from typing import List
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        index = 1
        dic = defaultdict(int)
        for s in strs:
            l = list(s)
            l.sort()
            l = "".join(l)
            t = dic[l]
            if t == 0:
                dic[l] = index
                ans.append([s])
                index += 1
            else:
                ans[t-1].append(s)
        return ans
if __name__ == "__main__":
    s = Solution()
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(s.groupAnagrams(strs))
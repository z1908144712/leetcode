from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrace(first = 0):
            if first == len(nums):
                ans.append(nums[:])
            for i in range(first, len(nums)):
                nums[i], nums[first] = nums[first], nums[i]
                backtrace(first + 1)
                nums[i], nums[first] = nums[first], nums[i]
        ans = []
        backtrace()
        return ans

if __name__ == "__main__":
    s = Solution()
    nums = [1, 2,3]
    print(s.permute(nums))
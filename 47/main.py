from typing import List
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrace(first = 0):
            if first == len(nums):
                ans.append(nums[:])
                return
            m = []
            for i in range(first, len(nums)):
                if nums[i] not in m:
                    m.append(nums[i])
                    #print(m)
                else:
                    continue
                #print(first*"\t",nums, first, i)
                nums[i], nums[first] = nums[first], nums[i]
                #print(first*"\t",nums, first, i)
                backtrace(first + 1)
                nums[i], nums[first] = nums[first], nums[i]
        ans = []
        nums.sort()
        backtrace()
        return ans

if __name__ == "__main__":
    s = Solution()
    nums = [0,1,0,0,9]
    print(s.permuteUnique(nums))
from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        maxIndex = start = count = 0
        while start < len(nums):
            end = start + nums[start] + 1
            #print(start, end)
            if end >= len(nums):
                return count + 1
            maxLen = nums[start]
            for n in range(start+1, end):
                if nums[n] > nums[maxIndex]:
                    maxIndex = n
                if (n - start + nums[n]) > maxLen:
                    maxLen = n - start + nums[n]
                    maxIndex = n
            if start == maxIndex:
                start += nums[start]
                maxIndex = start
            else:
                start = maxIndex
            count += 1
        return count

if __name__ == "__main__":
    s = Solution()
    nums = [4,1,1,3,1,1,1]
    print(s.jump(nums))
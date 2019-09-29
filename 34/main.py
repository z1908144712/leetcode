class Solution:
    def searchRange(self, nums: [int], target: int) -> [int]:
        left, right = 0, len(nums)-1
        first = last = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                first = last = mid
                while first > 0 and nums[first] == nums[first - 1]:
                    first -= 1
                while last < len(nums) - 1 and nums[last] == nums[last + 1]:
                    last += 1
                break
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        left, right = 0, len(nums)-1
        return [first, last]
if __name__ == "__main__":
    s = Solution()
    print(s.searchRange([1,1,2], 1))
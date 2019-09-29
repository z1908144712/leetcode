class Solution:
    def searchInsert(self, nums: [int], target: int) -> int:
        left, right = 0, len(nums)-1
        if target <= nums[left]:
            return left
        if target > nums[right]:
            return right + 1
        elif target == nums[right]:
            return right
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        if left <= right:
            return right
        else:
            return left

if __name__ == "__main__":
    s = Solution()
    print(s.searchInsert([1,3,5,6],0))
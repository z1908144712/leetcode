class Solution:
    def search(self, nums: [int], target: int) -> int:
        if len(nums) == 0:
            return -1
        maxIndex = 0
        while maxIndex < (len(nums) -1) and nums[maxIndex] <= nums[maxIndex+1]:
            maxIndex += 1
        if target > nums[maxIndex] or (maxIndex+1 < len(nums) and target < nums[maxIndex + 1]):
            return -1
        left, right = 0, len(nums)-1
        if target >= nums[left] and target <= nums[maxIndex]:
            right = maxIndex
        if maxIndex + 1 < len(nums) and target >= nums[maxIndex+1] and target <= nums[len(nums)-1]:
            left = maxIndex + 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return -1

if __name__ == "__main__":
    s = Solution()
    print(s.search([4,5,6,7,0,1,2], 3))
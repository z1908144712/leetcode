class Solution:
    def nextPermutation(self, nums) -> None:
        numsLen = len(nums)
        i = numsLen - 2
        while i >= 0 and nums[i+1] <= nums[i]:
            i -= 1
        if i >= 0 :
            j = numsLen -1
            while j>= 0 and nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        self.reverceNums(nums, i+1)
        return

    def reverceNums(self, nums, start) -> None:
        i, j = start, len(nums)-1
        while i < j :
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        return
    
    

if __name__ == "__main__":
    s = Solution()
    nums = [1,1,5]
    s.nextPermutation(nums)
    print(nums)
from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        ans, left, right, left_max, right_max = 0, 0, len(height) - 1, 0, 0
        while left < right:
            if height[left] < height[right]:
                if left_max <= height[left]:
                    left_max = height[left]
                else:
                    ans += left_max - height[left]
                left += 1
            else:
                if right_max <= height[right]:
                    right_max = height[right]
                else:
                    ans += right_max - height[right]
                right -= 1
        return ans

if __name__ == "__main__":
    s = Solution()
    print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
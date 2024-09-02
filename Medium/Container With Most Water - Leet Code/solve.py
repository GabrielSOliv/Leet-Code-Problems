class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        mArea = 0
        
        while left < right:
            currentMult = (right - left) * min(height[left], height[right])
            mArea = max(currentMult, mArea)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            
        return mArea

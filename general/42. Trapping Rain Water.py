class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        
        Instead of calculating area by height*width, we can think it in a cumulative way.
        In every iteration, keep left and right index, and leftMax and rightMax.
        If leftMax <= rightMax, (leftMax - height[left]) is the exact water we can store, 
        because if we have more water, it will leak from the left wall.
        """
        ans = 0
        left, right = 0, len(height) - 1
        leftMax, rightMax = 0, 0
        while left < right:
            leftMax = max(leftMax, height[left])
            rightMax = max(rightMax, height[right])
            if leftMax <= rightMax:
                ans += leftMax - height[left]
                left += 1
            else:
                ans += rightMax - height[right]
                right -= 1
        return ans
class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        
        1. As the area is based on width and height, 
        a long width is a good candidate;
        2. The shorter one of left and right doesn't support a higher level, 
        so can be removed from further consideration;
        """
        ans = 0
        left, right = 0, len(height) - 1
        while left != right:
            area = (right - left) * min(height[left], height[right])
            ans = max(ans, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return ans
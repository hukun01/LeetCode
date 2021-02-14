class Solution:
    def maxArea(self, height: List[int]) -> int:
        '''
        1. As the area is based on width and height, a long width is a good
           candidate;
        2. The shorter one of left and right doesn't support a higher level,
        so can be removed from further consideration;

        Time: O(n)
        Space: O(1)
        '''
        ans = 0
        l = 0
        r = len(height) - 1
        while l < r:
            ans = max((r - l) * min(height[l], height[r]), ans)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return ans
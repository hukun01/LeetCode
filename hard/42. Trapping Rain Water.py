# 42. Trapping Rain Water
class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        Instead of calculating area by height*width, we can think it in a
        cumulative way. In every iteration, keep left and right index, and
        left_max and right_max. Each iteration, we only focus on the lower end
        and the index. For example, if left_max <= right_max,
        (left_max - height[left]) is the exact water we can store,  because if
        we have more water, it will leak from the left(lower) wall.

        Time: O(n) where n is len(height).
        Space: O(1)
        '''
        ans = 0
        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        while left < right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])
            if left_max <= right_max:
                ans += left_max - height[left]
                left += 1
            else:
                ans += right_max - height[right]
                right -= 1
        return ans
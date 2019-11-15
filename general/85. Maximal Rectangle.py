class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        '''
        This is based on 84. Largets Rectangle in Histogram. We build the histogram 'heights' array
        for each row in the matrix, and use the 84 solution to find the max area.
        '''
        if not matrix or not matrix[0]:
            return 0
        heights = [1 if h == "1" else 0 for h in matrix[0]]
        maxArea = self.largestRectangleArea(heights)
        for row in matrix[1:]:
            for i in range(len(row)):
                if row[i] == "1":
                    heights[i] += 1
                else:
                    heights[i] = 0
            maxArea = max(maxArea, self.largestRectangleArea(heights))
        return maxArea
                
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        heights += [0] # less typing
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][0] >= h:
                prevH, prevStart = stack.pop()
                maxArea = max(maxArea, (i - prevStart) * prevH)
                start = prevStart
            stack.append((h, start))
        return maxArea
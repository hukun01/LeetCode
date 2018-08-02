class Solution:
    def kthSmallest(self, matrix, k):
        """
        Another instance for binary searching the value spaces.

        Total runtime is O(n * log(max - min))

        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        def countSmaller(matrix, target):
            count, j = 0, len(matrix[0]) - 1
            # each time j moves to left or down, so the runtime would be (row + col), aka, O(n)
            for i in range(len(matrix)):
                while j >= 0 and matrix[i][j] > m:
                    j -= 1
                count += j + 1
            return count
        
        l, h = matrix[0][0], matrix[len(matrix) - 1][len(matrix[0]) - 1] + 1
        while l < h: 
            m = (l + h) // 2
            if countSmaller(matrix, m) < k:
                l = m + 1
            else:
                h = m
        return l